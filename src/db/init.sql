-- =====================================================
-- Ember MVP – Worksheet Outputs Initialization
-- =====================================================

-- 1. Create table (idempotent)
create table if not exists public.worksheet_outputs (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null,
  worksheet jsonb not null,
  created_at timestamptz default now()
);

-- 2. Enable Row Level Security
alter table public.worksheet_outputs enable row level security;

-- =====================================================
-- 3. RLS POLICIES (User access)
-- =====================================================

-- Users can insert their own worksheets
do $$
begin
  if not exists (
    select 1 from pg_policies
    where schemaname = 'public'
      and tablename = 'worksheet_outputs'
      and policyname = 'Users can insert their own worksheets'
  ) then
    create policy "Users can insert their own worksheets"
    on public.worksheet_outputs
    for insert
    with check (auth.uid() = user_id);
  end if;
end
$$;

-- Users can read their own worksheets
do $$
begin
  if not exists (
    select 1 from pg_policies
    where schemaname = 'public'
      and tablename = 'worksheet_outputs'
      and policyname = 'Users can read their own worksheets'
  ) then
    create policy "Users can read their own worksheets"
    on public.worksheet_outputs
    for select
    using (auth.uid() = user_id);
  end if;
end
$$;

-- =====================================================
-- 4. RPC FUNCTION (Backend insert, RLS-safe)
-- =====================================================

create or replace function public.insert_worksheet_output(
  p_user_id uuid,
  p_worksheet jsonb
)
returns void
language plpgsql
security definer
as $$
begin
  insert into public.worksheet_outputs (user_id, worksheet)
  values (p_user_id, p_worksheet);
end;
$$;

-- Allow backend (service role) to execute RPC
grant execute on function public.insert_worksheet_output(uuid, jsonb)
to service_role;
