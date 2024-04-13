class DataTest:
    PERSON_ID = 1305

    STUDY_FIELD = '11.03.04 Электроника и наноэлектроника  - ФЭЛ'
    STUDY_PLAN = '11.03.04 Электроника и наноэлектроника (11.03.04_20_322.plx, 2023-2024) - каф.ЭПУ'

    MAPPING_DATA_TO_JSON = {
        "2,0,multiselect,0": {
            "code": "professional/areas/0/code",
            "value": "professional/areas/0/title"
        },
        "2,0,multiselect,2": "professional/tasks/0/title",
        "2,0,textarea_field,0": "professional/objects",
        "2,1,card,0,0": {
            "code": "professional/taskRows/0/value/0/code",
            "value": "professional/taskRows/0/value/0/title"
        },
        "2,1,card,0,1": "professional/taskRows/0/_children/0/value/title",
        "2,1,card,0,2": "professional/taskRows/0/_children/0/_children/0/value",
        "2,1,card,0,3": "professional/taskRows/0/_children/0/_children/1/value",
        "4,1,card,0,0": {
            "code": "programResults/generalProfessionalData/0/competence/cipher",
            "value": "programResults/generalProfessionalData/0/competence/title"
        },
        "4,1,card,0,1": {
            "code": "programResults/generalProfessionalData/0/indicators/0/cipher",
            "value": "programResults/generalProfessionalData/0/indicators/0/title"
        },
        "4,1,card,0,2": {
            "code": "programResults/generalProfessionalData/0/indicators/1/cipher",
            "value": "programResults/generalProfessionalData/0/indicators/1/title"
        },
        "4,2,card,0,1": {
            "code": "programResults/professionalData/competences/0/_children/0/competence/cipher",
            "value": "programResults/professionalData/competences/0/_children/0/competence/title"
        },
        "4,2,card,0,2": {
            "code": "programResults/professionalData/competences/0/_children/0/_children/0/competenceIndex/cipher",
            "value": "programResults/professionalData/competences/0/_children/0/_children/0/competenceIndex/title"
        },
        "4,2,card,1,1": "programResults/professionalData/objects/0/_children/0/object",
        "4,2,card,1,2": "programResults/professionalData/objects/0/_children/1/object",
        "4,2,card,2,1": "programResults/professionalData/bases/0/_children/0/base/title",
        "4,2,card,2,2": "programResults/professionalData/bases/0/_children/1/base/title",
        "5,0,input_field,0": "structure/structure/mainProcent",
        "5,0,input_field,1": "structure/structure/block1",
        "5,0,input_field,2": "structure/structure/block2",
        "5,0,input_field,3": "structure/structure/block3",
        "5,0,input_field,4": "structure/structure/all"
    }
