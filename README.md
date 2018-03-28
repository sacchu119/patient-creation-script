# Patient Creation Script

Steps to run the Patient Auto Insert Script

First thing to do is setting up Python and Oracle.

Installing Python.
1.	Install python 2.7 using this link https://www.python.org/downloads/release/python-2713/
(Use the Windows X86/X64)

2.	After Installation setup the environment variable by Right clicking on Computer -> Properties -> Advanced System Settings -> Environment Variables then under System variables double click on Path and add the New path of python installation folder (default will be ‘C:\Python27’) 
Installing Cx_Oracle. (Used to connect python to oracle database)
1.	Open command prompt as administrator  - python -m pip install cx_Oracle --upgrade
2.	Cx_oracle will be downloaded and added to library.
Installing oracle client (to do the database operations)
1.	Download an Oracle zip from here http://www.oracle.com/technetwork/topics/winx64soft-089540.html
2.	Unzip the package into a single directory that is accessible to your application, for example C:\oracle\instantclient_12_2.
3.	Set the environment variable PATH to include the path that you created in step 2. For example, on Windows 7, update PATH in Control Panel -> System -> Advanced System Settings -> Advanced -> Environment Variables -> System Variables -> PATH.
4.	If you have other Oracle software installed, then when you use Python you will need to make sure that the Instant Client directory, e.g. C:\oracle\instantclient_12_2, occurs in PATH before any other Oracle directories.
Setup is completed.

Creating the CSV
1.	Creating the CSV is easy an simple , first download the patient registration excel from JIRA .
2.	Make sure you keep a copy of the original for reference.
3.	Open the excel and first reorder the columns in the following order.
  a.	Last Name – You should add this new column and name it accordingly to your JIRA.
  b.	FirstName – Enter P1 and you can easily drag the mouse pointer to create its preceding values.(If you have the same patient with 2 Encounters use the same last name and first name, In the first row it will create the patient and add encounter. If the same patient name is found again it will only insert encounter)
  c.	Age – Don’t Enter any date just enter the age and the script will calculate the age according to today’s date.
  d.	Gender – If the test plan has only F and M , Please Find and replace it with MALE and FEMALE(Will update it sooner for taking input as F and M)
  e.	Encounter type – please check if the spelling of all types of encounter type is correct.
  f.	Building – this will change based on the domains we use because organization is created by someone else, so this script now has been set up for start organization we can update the script easily if we want to use organization also. So the name of the building for Start Building in CMTCERT is ‘START BLDG’
  g.	Nurse/Ambulatory – The same goes for this in CMTCERT so the NURSE/AMB name for Start office is ‘Start Office’(if you are confused about names you can search it in the code_value table and use those names, if you want to use different Nurse/AMB same goes for Building)
  h.	Arrive/admit/reg date time – Please make sure the date in this format ‘dd-MMM-YYYY HH:MM:SS’ for ex ’01-JAN-2018 23:59:59’(Please not you can format it by right clicking and FORMAT CELLS, You can select the whole column and do it in one shot)
  i.	Admit EP First Name – Check for Spelling.
  j.	Admit EP Last Name 
  k.	Attending EP First Name
  l.	Attending EP Last Name
  m.	Discharge time – again the same format as Arrive date time
  n.	Discharge Disp.
4.	You can leave the blank space if you don’t want to insert any fields like age usually, leave it blank don’t inset 0 and make sure you have left a field empty like the below.
5.	After all the above steps Save the Excel and Save as .csv and give any desired name.
6.	After Saving don’t open the CSV in excel application, because it will change the date format, to make sure the data is correct open the file in Notepad++ or any text editor.
7.	Creating of CSV is completed.

How to run the SCRIPT
1.	Download the archive from the mail (it contains all the code and extract it into any folder you like – remember we have set environment variable for python so we can run it anywhere.)
2.	 Open the folder where you have extracted the file Hold Shift + Right Click on open space -> Open command Window here.
3.	Type ‘Python addpatents.py’ and press ENTER(Without quotes) or double click and open.
4.	The Prompt will ask you to enter the path for CSV file. Please make sure you enter the full path (ex: C:\any_folder\test.csv)and press Enter.(Please enter the .csv extension without fail)
5.	If the file is not in the path or there is no data in the CSV it will show the error and the prompt will reappear till you Enter correct path and FILE.
6.	If you have any doubt if your CSV is correct or not, Please run it for test patient first, by changing the lastname in the CSV, If all the patients were inserted correctly you are good to go and update the last name with your JIRA number and run it again.
7.	All the patients will be created in very less time.
8.	Looks like bigger process when reading but once you do it, it’ll be easier from next time.
