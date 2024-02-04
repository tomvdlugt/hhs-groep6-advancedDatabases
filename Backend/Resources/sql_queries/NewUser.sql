-- drop the login if you like
-- MASTER
DROP LOGIN ReadonlyUsers
-- drop the user if you like
-- PlantenZiektenHerkenner
DROP USER Test_ReadOnlyUser
-- MASTER
-- Create the login on the MASTER database
CREATE LOGIN ReadonlyUsers WITH PASSWORD = '123321Pl@nt';
-- PlantenZiektenHerkenner
-- Create the suer on the desired-database
-- create the user itself
-- You will have to disconnect and reconnect directly to the database
CREATE USER Test_ReadOnlyUser FOR LOGIN ReadonlyUsers WITH DEFAULT_SCHEMA=[dbo]
GO
  -- alter role example from 
-- https://stackoverflow.com/questions/67691429/sql-readonly-access-permissions
ALTER ROLE db_datareader ADD MEMBER ReadonlyUsers;
GO
-- https://dba.stackexchange.com/questions/298493/is-there-a-simple-way-to-add-a-read-only-user
--grant select to pbi_reader  --grant select on whole database
--grant select on schema::dbo to pbi_reader  --grant select on one schema
grant select on [dbo].[UploadedImages] to Test_ReadOnlyUser  --grant select on one table database
grant select on [dbo].[checks] to Test_ReadOnlyUser  --grant select on one table database
--deny select on dbo.user_membership to Test_ReadOnlyUser --override the grant with a deny for one table
deny insert on [dbo].[UploadedImages] to Test_ReadOnlyUser --override the grant with a deny for one table