import re
import cx_Oracle
from datetime import datetime
from datetime import timedelta
from dataFetcher import dataFetcher
from connect import connect
###########################################################
# Inserting the data to database
###########################################################

class dataInserter:
    def insertPerson(self,patientData):
        print 'Inserting Person'
        personId = patientData['person_id']
        firstName = patientData['firstname']
        lastName = patientData['lastname']
        age = str(patientData['age'])
        sex = patientData['sex']
        dataFetch = dataFetcher()
        gender = str(dataFetch.getCodeValue("DISPLAY_KEY" ,'57',patientData['sex']))
        ethincGroupCode = dataFetch.getCodeValue('DISPLAY_KEY' ,'27' ,'MULTIPLE')
        mrnOne = dataFetch.getCodeValue('DISPLAY_KEY' ,'263' ,'MRN')
        mrnTwo = dataFetch.getCodeValue('DISPLAY_KEY' ,'4' ,'MRN')
        raceCode = dataFetch.getCodeValue('DISPLAY_KEY' ,'282' ,'ASIAN')
        active = dataFetch.getCodeValue('DISPLAY_KEY' ,'48' ,'ACTIVE' )

        if(not age):
            dob = ''
        else:
            calculatedDate = datetime.now() - timedelta(days=(int(age)*365 + int(age)/4), hours = 13)
            dob = datetime.strptime(str(calculatedDate),'%Y-%m-%d %H:%M:%S.%f').strftime('%d-%b-%Y %H:%M:%S')
        insertPersonString = ('insert into person'
                        '( person_id ,'
                        'updt_cnt , '
                        'updt_dt_tm ,'
                        'updt_id ,'
                        'updt_task ,'
                        'active_ind ,'
                        'active_status_cd ,'
                        'active_status_dt_tm ,'
                        'beg_effective_dt_tm ,'
                        'end_effective_dt_tm ,'
                        'name_last_key ,'
                        'name_first_key ,'
                        'name_full_formatted ,'
                        'birth_dt_tm ,'
                        'cause_of_death ,'
                        'deceased_cd ,'
                        'deceased_dt_tm ,'
                        'ethnic_grp_cd ,'
                        'language_cd ,'
                        'race_cd ,'
                        'sex_cd ,'
                        'name_last ,'
                        'name_first ,'
                        'abs_birth_dt_tm ,'
                        'logical_domain_id)'
                        'values'
                        '(' + personId + ','
                        '1,'
                        'sysdate,'
                        '1234,'
                        '1234,'
                        '1,'
                        + active +','
                        'sysdate,'
                        'sysdate,'
                        'to_date(\'31-DEC-2100 23:59:59\',\'DD-MON-RRRR HH24:MI:SS\'),'
                        'UPPER(\''+ re.sub('[^a-zA-Z0-9 \n\.]', '', lastName) +'\'),'
                        'UPPER(\''+ re.sub('[^a-zA-Z0-9 \n\.]', '', firstName) +'\'),'
                        '\''+ lastName + ', '+ firstName +'\','
                        'to_date(\'' + dob +'\',\'DD-MON-RRRR HH24:MI:SS\')  + 6/24,'
                        'null,'
                        '0,'
                        'null,'
                        + ethincGroupCode + ','
                        '0 ,'
                        + raceCode + ','
                        + gender +','
                        '\''+ lastName +'\','
                        '\''+ firstName +'\','
                        'to_date(\'' + dob +'\',\'DD-MON-RRRR HH24:MI:SS\')  + 6/24,'
                        '0)'
                        )
        insertPersonAlias = ('insert into person_alias('
                             'person_alias_id,'
                             'person_id,'
                             'updt_cnt,'
                             'updt_dt_tm,'
                             'active_ind,'
                             'alias_pool_cd,'
                             'person_alias_type_cd,'
                             'alias)'
                             'VALUES('
                             '(SELECT max(person_alias_id) FROM person_alias) + 1,'
                             + personId + ','
                             '0 ,'
                             'sysdate,'
                             '1,'
                             + mrnOne +','
                             + mrnTwo +','
                             'to_char(reference_seq.nextval))'
                                )
        #print insertPersonString +'\n'
        #print insertPersonAlias +'\n'
        try:
            connectionObj = connect()
            connection = connectionObj.getConnection()
            cursor = connection.cursor()
            cursor.execute(insertPersonString)
            connection.commit()
            cursor.execute(insertPersonAlias)
            connection.commit()
            connectionObj.disconnect(connection,cursor)
        except cx_Oracle.DatabaseError as exception:
            print('Error occurred while inserting ' + lastName + ', ' +firstName + ' to database')

        

####Insert alias
    def insertEncounter(self,patientData):
        print 'Inserting Encounter........'
        dataFetch = dataFetcher()
        firstName = patientData['firstname']
        lastName = patientData['lastname']
        arriveDate = patientData['arrive_dt_tm']
        regDate = patientData['arrive_dt_tm']
        admitDate = patientData['arrive_dt_tm']
        encounterType = patientData['encounter_type']
        classVar = str(dataFetch.getCodeValue('DISPLAY_KEY','321',encounterType.upper()))
        typeVar = str(dataFetch.getCodeValue('DISPLAY_KEY','71',encounterType.upper()))
        typeClassVar = str(dataFetch.getCodeValue('CDF_MEANING','69',encounterType))
        building = patientData['building']
        pos = patientData['pos']
        buildingCode = str(dataFetch.getCodeValue('DISPLAY_KEY','220',building.upper().replace(' ','')))
        posCode = str(dataFetch.getCodeValue('DISPLAY_KEY','220',pos.upper().replace(' ','')))
        dischargeDate = patientData['disch_dt_tm']
        dischargeDisposition = patientData['disch_dis']
        dischargeDispCode = str(dataFetch.getCodeValue('DISPLAY_KEY','19',dischargeDisposition.upper().replace(' ','')))
        admitPhysicianFirst = patientData['admit_EP_firstname']
        admitPhysicianLast = patientData['admit_EP_lastname']
        attendingPhysicianFirst = patientData['attend_EP_firstname']
        attendingPhysicianLast = patientData['attend_EP_lastname']
        encounterId = dataFetch.getNextId('encounter','encntr_id')
        nameLastKey = re.sub('[^a-zA-Z0-9 \n\.]', '', patientData['lastname'])
        nameFirstKey = re.sub('[^a-zA-Z0-9 \n\.]', '', patientData['firstname'])
        finClassCode = dataFetch.getCodeValue('DISPLAY_KEY' ,'354' ,'CHAMPUS')
        relationTypeOne = dataFetch.getCodeValue('DISPLAY' ,'333' ,'Attending Physician' )
        relationTypeTwo = dataFetch.getCodeValue('DISPLAY' ,'333' ,'Admitting Physician' )
        relationTypeThree = dataFetch.getCodeValue('DISPLAY' ,'331','Family Physician' )
        active = dataFetch.getCodeValue('DISPLAY_KEY' ,'48' ,'ACTIVE' )
        maxDate = '31-DEC-2100 23:59:59'
        Facility = dataFetch.getCodeValue('DISPLAY_KEY' ,'220' ,'STARTORG' )
        if(Facility == 0):
            Facility = dataFetch.getCodeValue('DESCRIPTION' ,'220' ,'START Organization' )
        aliasPool = dataFetch.getCodeValue('DISPLAY' ,'263' ,'FINNUMBER' )
        if(aliasPool == 0):
            aliasPool = dataFetch.getCodeValue('DISPLAY_KEY' ,'263' ,'FIN' )
        aliasTypeVar = dataFetch.getCodeValue('DISPLAY_KEY' ,'263' ,'FINNBR')
        
        insertEncounterString = ('INSERT into encounter '
                                     '(encntr_id ,'
                                     'person_id ,'
                                     'updt_cnt ,'
                                     'updt_dt_tm ,'
                                     'updt_id ,'
                                     'updt_task ,'
                                     'active_ind ,'
                                     'active_status_cd ,'
                                     'active_status_dt_tm ,'
                                     'beg_effective_dt_tm ,'
                                     'end_effective_dt_tm ,'
                                     'encntr_type_cd ,'
                                     'encntr_type_class_cd ,'
                                     'reg_dt_tm ,'
                                     'arrive_dt_tm ,'
                                     'inpatient_admit_dt_tm ,'
                                     'location_cd ,'
                                     'loc_facility_cd ,'
                                     'loc_building_cd ,'
                                     'loc_nurse_unit_cd ,'
                                     'organization_id ,'
                                     'financial_class_cd,'
                                     'disch_dt_tm ,'
                                     'disch_disposition_cd )'
                                     'VALUES(' + encounterId + ','
                                     '(SELECT p.person_id FROM person p WHERE p.name_first_key = \'' + nameFirstKey.upper() + '\' AND p.name_last_key = \'' + nameLastKey.upper() + '\'),'
                                     '0 ,'
                                     'sysdate,'
                                     '1234 ,'
                                     '1234 ,'
                                     '1 ,'
                                     + active + ','
                                     'sysdate,'
                                     'sysdate,'
                                     'to_date(\'' + maxDate +'\',\'DD-MON-RRRR HH24:MI:SS\'),'
                                     + typeVar + ','
                                     + typeClassVar + ','
                                     'to_date(\'' + regDate +'\',\'DD-MON-RRRR HH24:MI:SS\') + 6/24,'
                                     'to_date(\'' + arriveDate +'\',\'DD-MON-RRRR HH24:MI:SS\')  + 6/24,'
                                     'to_date(\'' + admitDate +'\',\'DD-MON-RRRR HH24:MI:SS\') + 6/24,'
                                     + Facility +','
                                     + Facility +','
                                     + buildingCode + ','
                                     + posCode + ','
                                     '(SELECT organization_id FROM organization WHERE org_name_key = \'STARTORGANIZATION\'),'
                                     + finClassCode +','
                                     'to_date(\'' + dischargeDate +'\',\'DD-MON-RRRR HH24:MI:SS\') + 6/24,'
                                     + dischargeDispCode + ')'
                                 )
        insertEncounterAlias = (
                            'INSERT into encntr_alias'
                            '(encntr_alias_id ,'
                            'encntr_id ,'
                            'updt_cnt ,'
                            'updt_dt_tm ,'
                            'updt_id ,'
                            'updt_task ,'
                            'active_ind ,'
                            'alias_pool_cd ,'
                            'encntr_alias_type_cd ,'
                            'alias ,'
                            'beg_effective_dt_tm ,'
                            'end_effective_dt_tm )'
                            'VALUES('
                            '(select max(encntr_alias_id + 1) from encntr_alias),'
                            + encounterId + ','
                            '0 ,'
                            'sysdate,'
                            '1234,'
                            '1234,'
                            '1 ,'
                            + aliasPool +','
                            + aliasTypeVar +','
                            'to_char(reference_seq.nextval),'
                            'sysdate,'
                            'to_date(\'' + maxDate +'\',\'DD-MON-RRRR HH24:MI:SS\'))'
                            )
        insertEncounterPrsnlRelAttend = (
                                    'INSERT into encntr_prsnl_reltn'
                                   '(encntr_prsnl_reltn_id ,'
                                   'prsnl_person_id ,'
                                   'encntr_prsnl_r_cd ,'
                                   'encntr_id ,'
                                   'updt_cnt ,'
                                   'updt_dt_tm ,'
                                   'updt_id ,'
                                   'updt_task ,'
                                   'active_ind ,'
                                   'beg_effective_dt_tm ,'
                                   'end_effective_dt_tm ,'
                                   'encntr_type_cd )'
                                   'VALUES('
                                   '(select max(encntr_prsnl_reltn_id) + 1 from encntr_prsnl_reltn),'
                                   '(SELECT person_id FROM prsnl p WHERE p.name_first_key = \'' + attendingPhysicianFirst.upper() + '\' AND p.name_last_key = \'' + attendingPhysicianLast.upper() + '\'),'
                                   + relationTypeOne +','
                                   + encounterId +','
                                   '0 ,'
                                   'sysdate,'
                                   '1234 ,'
                                   '1234 ,'
                                   '1 ,'
                                   'to_date(\'' + arriveDate +'\',\'DD-MON-RRRR HH24:MI:SS\') + 6/24,'
                                   'to_date(\'' + maxDate +'\',\'DD-MON-RRRR HH24:MI:SS\'),'
                                   + typeVar + ')'
                                    )

        insertEncounterPrsnlRelAdmit = (
                                    'INSERT into encntr_prsnl_reltn'
                                   '(encntr_prsnl_reltn_id ,'
                                   'prsnl_person_id ,'
                                   'encntr_prsnl_r_cd ,'
                                   'encntr_id ,'
                                   'updt_cnt ,'
                                   'updt_dt_tm ,'
                                   'updt_id ,'
                                   'updt_task ,'
                                   'active_ind ,'
                                   'beg_effective_dt_tm ,'
                                   'end_effective_dt_tm ,'
                                   'encntr_type_cd )'
                                   'VALUES('
                                   '(select max(encntr_prsnl_reltn_id) + 1 from encntr_prsnl_reltn),'
                                   '(SELECT person_id FROM prsnl p WHERE p.name_first_key = \'' + admitPhysicianFirst.upper() + '\' AND p.name_last_key = \'' + admitPhysicianLast.upper() + '\'),'
                                   + relationTypeTwo +','
                                   + encounterId +','
                                   '0 ,'
                                   'sysdate,'
                                   '1234 ,'
                                   '1234 ,'
                                   '1 ,'
                                   'to_date(\'' + arriveDate +'\',\'DD-MON-RRRR HH24:MI:SS\') + 6/24,'
                                   'to_date(\'' + maxDate +'\',\'DD-MON-RRRR HH24:MI:SS\'),'
                                    + typeVar + ')'
                                    )
##        print insertEncounterString +'\n'
##        print insertEncounterAlias +'\n'
##        print insertEncounterPrsnlRelAttend +'\n'
##        print insertEncounterPrsnlRelAdmit +'\n'

        
        connectionObj = connect()
        connection = connectionObj.getConnection()
        cursor = connection.cursor()
        cursor.execute(insertEncounterString)
        connection.commit()
        #print 'Encounter'
        cursor.execute(insertEncounterAlias)
        connection.commit()
        #print 'Encounter Alias'
        cursor.execute(insertEncounterPrsnlRelAttend)
        connection.commit()
        #print 'Encounter EP Relation - Attending Physician'
        cursor.execute(insertEncounterPrsnlRelAdmit)
        connection.commit()
        #print 'Encounter EP Relation - Admitting Physician'
        connection.commit()
        connectionObj.disconnect(connection,cursor)
        print 'All the data for patient ' + lastName + ', ' + firstName + ' was successfully inserted'
