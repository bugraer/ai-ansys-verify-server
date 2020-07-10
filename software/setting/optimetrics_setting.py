def optimetrics_setting(ctx):
    current     = ctx["response"]["corner_point"]["current"]
    speed       = ctx["response"]["corner_point"]["speed"]
    wmw         = ctx["data"]["spec_params"]["wmw"]
    wmt         = ctx["data"]["spec_params"]["wmt"]
    am          = ctx["data"]["spec_params"]["am"]
    delta       = ctx["data"]["spec_params"]["delta"]
    rotor_arc   = ctx["data"]["spec_params"]["R1"]
    opt_name    = ctx["data"]["opt_name"]
    opt_oModule = ctx["ansys_object"]["oDesign"].GetModule("Optimetrics")

    def opt_setting():
        opt_oModule.InsertSetup("OptiParametric",
                            [
                                "NAME:" + opt_name,
                                "IsEnabled:="		, True,
                                [
                                    "NAME:ProdOptiSetupData",
                                    "SaveFields:="		, False,
                                    "CopyMesh:="		, False
                                ],
                                [
                                    "NAME:StartingPoint"
                                ],
                                "Sim. Setups:="		, ["setup1"],
                                [
                                        "NAME:Sweeps",
                                    [
                                            "NAME:SweepDefinition",
                                            "Variable:="		, "Irms",
                                            "Data:="		, str(current) + "A",
                                            "OffsetF1:="		, False,
                                            "Synchronize:="		, 0
                                    ],
                                    [
                                            "NAME:SweepDefinition",
                                            "Variable:="		, "Sp",
                                            "Data:="		, str(speed) + "rpm",
                                            "OffsetF1:="		, False,
                                            "Synchronize:="		, 0
                                    ],
                                    [
                                            "NAME:SweepDefinition",
                                            "Variable:="		, "delta",
                                            "Data:="		, str(delta) + "deg",
                                            "OffsetF1:="		, False,
                                            "Synchronize:="		, 0
                                    ],
                                    [
                                            "NAME:SweepDefinition",
                                            "Variable:="		, "wmw",
                                            "Data:="		, str(wmw) + "mm",
                                            "OffsetF1:="		, False,
                                            "Synchronize:="		, 0
                                    ],
                                    [
                                            "NAME:SweepDefinition",
                                            "Variable:="		, "wmt",
                                            "Data:="		, str(wmt) + "mm",
                                            "OffsetF1:="		, False,
                                            "Synchronize:="		, 0
                                    ],
                                    [
                                            "NAME:SweepDefinition",
                                            "Variable:="		, "R1",
                                            "Data:="		, str(rotor_arc)+ "mm",
                                            "OffsetF1:="		, False,
                                            "Synchronize:="		, 0
                                    ]
                                ],
                                [
                                        "NAME:Sweep Operations",
                                ],
                                [
                                    "NAME:Goals"
                                ]
                            ])

#     def opt_re_setting(var_name, var_data):
#         opt_oModule.EditSetup(opt_name,
#                           [
#                               "NAME:" + opt_name,
#                               "IsEnabled:="		, True,
#                               [
#                                   "NAME:ProdOptiSetupData",
#                                   "SaveFields:="		, False,
#                                   "CopyMesh:="		, False
#                               ],
#                               [
#                                   "NAME:StartingPoint"
#                               ],
#                               "Sim. Setups:="		, ["setup1"],
#                               [
#                                   "NAME:Sweeps",
#                                   [
#                                       "NAME:SweepDefinition",
#                                       "Variable:="	, var_name,
#                                       "Data:="		, var_data,
#                                       "OffsetF1:="	, False,
#                                       "Synchronize:="	, 0
#                                   ]
#                               ],
#                               [
#                                   "NAME:Sweep Operations"
#                               ],
#                               [
#                                   "NAME:Goals"
#                               ]
#                           ])

    # exec
    opt_setting()

    # if reset == 'set_first_time':
    #     list(map(opt_setting,
    #              opt_name_list, opt_data_list
    #              ))
    # else:
    #     list(map(opt_re_setting,
    #              opt_name_list, opt_data_list
    #              ))

    ctx["data"]["opt_oModule"] = opt_oModule

    return ctx

def start_analysis(ctx):
    print('Start Analysis')

    ctx["data"]["opt_oModule"].SolveSetup(ctx["data"]["opt_name"])

    return ctx

def delete_opt_setting(ctx):
    print('remove opt setting')
    ctx["data"]["opt_oModule"].DeleteSetups([ctx["data"]["opt_name"]])

    return ctx