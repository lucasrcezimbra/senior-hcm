import pytest


@pytest.fixture
def user_id():
    return "0987654321LMNOPQRSTUVWXYZABCDEFG"


@pytest.fixture
def login_response_mock(user_id):
    return {
        "isLoggedIn": True,
        "session": {
            "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456",
            "tenantId": "emp",
            "username": "fulano.silva",
            "email": "example@mail.com",
            "personId": "1234567890ABCDEFGHIJKLMNOPQRSTUV",
            "personFirstName": "Fulano",
            "personMiddleName": "da",
            "personLastName": "Silva",
            "personPhotoLink": "https://senior-hcm-storage.s3.sa-east-1.amazonaws.com/emp/attachment/ABCDEFGHIJKLMNOPQRSTUVWXYZ123456/person-photo/1234567890ABCDEFGHIJKLMNOPQRSTUV",
            "employees": [
                {
                    "id": user_id,
                    "jobPosition": "Programador(a)",
                    "userRoles": [
                        {
                            "name": "Colaborador",
                            "userRoleType": "EMPLOYEE",
                            "userRoleId": "MNOPQRSTWXYZ0987654321ABCDEFGHIJ",
                        }
                    ],
                    "situation": "ACTIVE",
                }
            ],
            "forcePasswordChange": False,
            "contactEmail": "example@mail.com",
            "g7Tenant": "emp",
        },
        "developmentControl": [
            "MANTER_TREINAMENTO",
            "MANTER_EXPERIENCIA_PROFISSIONAL",
            "MANTER_CONTATO_EMERGENCIA",
            "MANTER_ENDERECOS_PESSOAIS",
            "CADASTRAR_LOCALIZACAO",
            "MOSTRAR_ANOTACOES_DA_FICHA_CADASTRO",
            "MANTER_CONTATOS_PESSOAIS",
            "MANTER_DADOS_PESSOAIS",
            "MANTER_DEPENDENTE",
            "MOSTRAR_SALARIOS_PARA_O_GESTOR",
            "FEEDBACK_EVALUATOR",
            "MANTER_REG_PROFISSIONAL",
            "MANTER_PROJETOS",
            "MANTER_FORMACAO_ACADEMICA",
            "EXIBIR_ANIVERSARIANTES",
            "MANTER_DOCUMENTOS_PESSOAIS",
            "EXIBE_DESCRICAO_DO_CARGO",
            "OBRIGAR_PRAZO_OBJETIVO_DESENVOLVIMENTO",
            "MANTER_INTERESSE_PESSOAL",
            "MANTER_CERTIFICACAO",
            "MOVIMENTACOES",
        ],
        "localization": {
            "id": "EFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJ",
            "name": "Português (Brasileiro)",
            "dateFormat": "dd/mm/aaaa",
            "language": "PT_BR",
            "isDefault": True,
            "onlyAdmin": False,
        },
        "menus": [
            {
                "employee": user_id,
                "roles": [
                    {
                        "role": "MNOPQRSTWXYZ0987654321ABCDEFGHIJ",
                        "roleType": "EMPLOYEE",
                        "menus": [
                            {
                                "name": "my-contract",
                                "stateName": "my-contract",
                                "title": "Contrato de trabalho",
                                "icon": "fa-file-text",
                                "order": 300,
                                "children": [
                                    {
                                        "name": "employee-management.time-tracking",
                                        "stateName": "employee-management.time-tracking",
                                        "title": "Cartão ponto",
                                        "icon": "fa-clock-o",
                                        "order": 700,
                                    },
                                    {
                                        "name": "profile.timeline",
                                        "stateName": "profile.timeline",
                                        "title": "Histórico profissional",
                                        "icon": "fa-history",
                                        "order": 400,
                                    },
                                    {
                                        "name": "profile.dependents",
                                        "stateName": "profile.dependents",
                                        "title": "Ficha familiar",
                                        "icon": "fa-child",
                                        "order": 500,
                                    },
                                    {
                                        "name": "profile.contract",
                                        "stateName": "profile.contract",
                                        "title": "Meu contrato de trabalho",
                                        "icon": "fa-file-text",
                                        "order": 300,
                                    },
                                    {
                                        "name": "profile.salary-evolution",
                                        "stateName": "profile.salary-evolution",
                                        "title": "Evolução salarial",
                                        "icon": "fa-line-chart",
                                        "order": 200,
                                    },
                                    {
                                        "name": "profile.annual-wage-summary",
                                        "stateName": "profile.annual-wage-summary",
                                        "title": "Minha remuneração anual",
                                        "icon": "fa-bar-chart",
                                        "order": 100,
                                    },
                                    {
                                        "name": "profile.wage",
                                        "stateName": "profile.wage",
                                        "title": "Demonstrativos de pagamento",
                                        "icon": "fa-file-text-o",
                                        "order": 0,
                                    },
                                ],
                            },
                            {
                                "name": "structure",
                                "stateName": "structure",
                                "title": "Estrutura organizacional",
                                "icon": "fa-building-o",
                                "order": 500,
                                "children": [
                                    {
                                        "name": "hierarchy",
                                        "stateName": "hierarchy",
                                        "title": "Hierarquia",
                                        "icon": "fa-sitemap",
                                        "order": 100,
                                    }
                                ],
                            },
                            {
                                "name": "profile",
                                "stateName": "profile.personal",
                                "title": "Meu perfil",
                                "icon": "fa-user",
                                "order": 100,
                                "children": [
                                    {
                                        "name": "profile.personal",
                                        "stateName": "profile.personal",
                                        "title": "Dados pessoais",
                                        "icon": "fa-user",
                                        "order": 0,
                                    },
                                    {
                                        "name": "profile.professional",
                                        "stateName": "profile.professional",
                                        "title": "Perfil profissional",
                                        "icon": "fa-book",
                                        "order": 100,
                                    },
                                    {
                                        "name": "profile.education",
                                        "stateName": "profile.education",
                                        "title": "Perfil acadêmico",
                                        "icon": "fa-graduation-cap",
                                        "order": 200,
                                    },
                                    {
                                        "name": "profile.interest",
                                        "stateName": "profile.interest",
                                        "title": "Interesses pessoais",
                                        "icon": "fa-heart",
                                        "order": 300,
                                    },
                                    {
                                        "name": "public",
                                        "stateName": "profile.perfil-public",
                                        "title": "Perfil público",
                                        "icon": "fa-globe",
                                        "order": 999,
                                    },
                                ],
                            },
                            {
                                "name": "settings",
                                "stateName": "settings.authentication",
                                "title": "Opções",
                                "icon": "fa-wrench",
                                "order": 2,
                            },
                            {
                                "name": "vacation",
                                "stateName": "vacation",
                                "title": "Férias",
                                "icon": "fa-plane",
                                "order": 300,
                                "children": [
                                    {
                                        "name": "vacation.calendar",
                                        "stateName": "vacation.calendar",
                                        "title": "Calendário",
                                        "icon": "fa-calendar",
                                        "order": 0,
                                    },
                                    {
                                        "name": "vacation.employee",
                                        "stateName": "vacation.employee",
                                        "title": "Minhas férias",
                                        "icon": "fa-plane",
                                        "order": 600,
                                    },
                                ],
                            },
                            {
                                "name": "myteam",
                                "stateName": "myteam",
                                "title": "Minha equipe",
                                "icon": "fa-users",
                                "order": 400,
                            },
                            {
                                "name": "dashboard",
                                "stateName": "dashboard",
                                "title": "Painel",
                                "icon": "fa-dashboard",
                                "order": 0,
                            },
                        ],
                    }
                ],
            }
        ],
        "timeToExpireSession": 20,
        "modules": ["MANAGEMENT_PANEL"],
    }


@pytest.fixture
def payrolls_response_mock(user_id):
    return {
        "list": [
            {
                "id": "40401234567890987654321",
                "calculation": {
                    "id": "72098765432123456789ABC",
                    "paymentDate": "2019-04-05",
                    "paymentReference": "2019-03",
                    "type": "CALCULO_MENSAL",
                    "reportLink": "https://folha.emp.com.br:8000/abcdweb/",
                },
                "employee": {"id": user_id},
                "details": {
                    "paymentType": "BANK_DEPOSIT",
                    "bankPayment": [
                        {"bank": "BANCO BANK", "agency": "0001", "account": "0123-4"}
                    ],
                },
                "netValue": 8000.00,
                "referenceSalary": 10000,
                "quantidadeDependentesParaImpostoRenda": 0,
                "quantidadeDependentesParaSalarioFamilia": 0,
                "valorBaseINSS": 10000,
                "valorBaseIR": 10000,
                "valorBaseFGTS": 10000,
                "currency": "REAL",
                "wageTypes": [
                    {
                        "id": "632456789OASDYSDIUVFDS",
                        "wageType": {
                            "id": "ABCOIUER09123485789837142",
                            "name": "Salário Mensalista",
                            "type": "PROCEEDS",
                            "kind": "HORAS_TRABALHADAS_NO_MES",
                        },
                        "referenceValue": 200.17,
                        "actualValue": 9000.99,
                    },
                    {
                        "id": "ASDFOASDIF01239488913428",
                        "wageType": {
                            "id": "8ASDKFDSAIO348JKSJKSDFJ938",
                            "name": "INSS",
                            "type": "DEDUCTION",
                            "kind": "UNCLASSIFIED_INFORMATIVE",
                        },
                        "referenceValue": 11.0,
                        "actualValue": 1100,
                    },
                    {
                        "id": "OASDFJAOSIDF03124123948",
                        "wageType": {
                            "id": "12938198523KJSFHLKFS",
                            "name": "IRRF",
                            "type": "DEDUCTION",
                            "kind": "UNCLASSIFIED_INFORMATIVE",
                        },
                        "referenceValue": 27.5,
                        "actualValue": 2750,
                    },
                    {
                        "id": "777OIAUSOIUSOI1324198324",
                        "wageType": {
                            "id": "5EOISAUOISUFIOSAFUUOI876127612",
                            "name": "Unimed - Titular",
                            "type": "DEDUCTION",
                            "kind": "UNCLASSIFIED_INFORMATIVE",
                        },
                        "referenceValue": 0.0,
                        "actualValue": 200.01,
                    },
                    {
                        "id": "195OIUOIYTTGJB439814375",
                        "wageType": {
                            "id": "22BBDDOEOIHDHHFHSA18974",
                            "name": "Vale Refeição",
                            "type": "DEDUCTION",
                            "kind": "UNCLASSIFIED_INFORMATIVE",
                        },
                        "referenceValue": 20.0,
                        "actualValue": 200.0,
                    },
                ],
                "valorFGTS": 1000.0,
                "graphic": [
                    {"name": "DEDUCTION", "data": [2000.81]},
                    {"name": "PROCEEDS", "data": [10000.0]},
                ],
            },
        ],
        "isMoreItemsAvailable": True,
        "linkNextPage": f"https://hcm-api.senior.com.br/frontend-api/payrollregister/recents/{user_id}?lastId=9132847198234KJAFDSHJFKADSF&lastPaymentDay=2019-02-06",
    }
