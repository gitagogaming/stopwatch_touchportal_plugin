{"FF":"Default","A":[{"KEY_STATE_TRUEFALSE":false,"KEY_STATE_VALUE_TYPE":0,"KEY_STATE_COMPARISON":"=","kIEn":true,"KEY_STATE_STRING_VALUE":"Off","KEY_STATE_NAME":"self","KEY_TYPE":"LOGIC_IF_ACTION"},{"KEY_STATE_TRUEFALSE":true,"kIEn":true,"KEY_TYPE":"LOGIC_SET_BUTTON_STATE_ACTION"},{"kPlugType":2,"kID":"tp.plugin.Gitago.Stopwatch.act.start_stopwatch","kPrefix":"Stopwatch: START / STOP","kInline":"false","kHHF":"false","kcD":-14342324,"kPID":"tp.plugin.Gitago.Stopwatch","kData":[{"default":"Start","id":"tp.plugin.Gitago.Stopwatch.act.status","label":"Text","valueChoices":["Start","Stop","Pause","Resume"],"type":"choice"},{"default":"0","id":"tp.plugin.Gitago.Stopwatch.act.stopwatch_name","label":"stop watch name","type":"text"}],"kVals":[{"VAL":"Start","ID":"tp.plugin.Gitago.Stopwatch.act.status","TYPE":"choice"},{"VAL":"1","ID":"tp.plugin.Gitago.Stopwatch.act.stopwatch_name","TYPE":"text"}],"kStatic":"false","kcL":-9405771,"ksLI":-1,"kET":0,"KEY_TYPE":"PLUGIN_ACTION","kFormat":"Turn your Stopwatch On, or Off {$tp.plugin.Gitago.Stopwatch.act.status$} with the ID {$tp.plugin.Gitago.Stopwatch.act.stopwatch_name$}","kName":"Stopwatch: START / STOP","ksLILW":-1},{"kIEn":true,"KEY_TYPE":"LOGIC_ELSE_ACTION"},{"KEY_STATE_TRUEFALSE":false,"kIEn":true,"KEY_TYPE":"LOGIC_SET_BUTTON_STATE_ACTION"},{"kPlugType":2,"kID":"tp.plugin.Gitago.Stopwatch.act.start_stopwatch","kPrefix":"Stopwatch: START / STOP","kInline":"false","kHHF":"false","kcD":-14342324,"kPID":"tp.plugin.Gitago.Stopwatch","kData":[{"default":"Start","id":"tp.plugin.Gitago.Stopwatch.act.status","label":"Text","valueChoices":["Start","Stop","Pause","Resume"],"type":"choice"},{"default":"0","id":"tp.plugin.Gitago.Stopwatch.act.stopwatch_name","label":"stop watch name","type":"text"}],"kVals":[{"VAL":"Pause","ID":"tp.plugin.Gitago.Stopwatch.act.status","TYPE":"choice"},{"VAL":"1","ID":"tp.plugin.Gitago.Stopwatch.act.stopwatch_name","TYPE":"text"}],"kStatic":"false","kcL":-9405771,"ksLI":-1,"kET":0,"KEY_TYPE":"PLUGIN_ACTION","kFormat":"Turn your Stopwatch On, or Off {$tp.plugin.Gitago.Stopwatch.act.status$} with the ID {$tp.plugin.Gitago.Stopwatch.act.stopwatch_name$}","kName":"Stopwatch: START / STOP","ksLILW":-1},{"kIEn":true,"KEY_TYPE":"LOGIC_IF_END_ACTION"}],"BD":1,"C":[],"BE":-16777216,"kSCM":25,"BG":-13421773,"E":[{"kTxt":"Status:${value:tp.plugin.Gitago.Stopwatch.states.STATUS.1}\nElapsed:${value:tp.plugin.Gitago.Stopwatch.states.time_elapsed.1}","KEY_TYPE":"AUTO_UPDATE_EVENT"},{"KEY_STATE_DESCRIPTION":"On state changes to","kPSC":true,"KEY_IS_NOT_EQUAL":false,"kCSC":0,"KEY_STATE":"RESET","KEY_STATE_ID":"tp.plugin.Gitago.Stopwatch.states.STATUS.1","KEY_TYPE":"ON_STATE_AWARENESS_CHANGE","kICustom":false},{"KEY_STATE_TRUEFALSE":false,"kIEn":true,"KEY_TYPE":"LOGIC_SET_BUTTON_STATE_ACTION"},{"KEY_STATE_DESCRIPTION":"On state changes to","kPSC":true,"KEY_IS_NOT_EQUAL":false,"kCSC":0,"KEY_STATE":"PAUSED","KEY_STATE_ID":"tp.plugin.Gitago.Stopwatch.states.STATUS.1","KEY_TYPE":"ON_STATE_AWARENESS_CHANGE","kICustom":false},{"KEY_STATE_TRUEFALSE":false,"kIEn":true,"KEY_TYPE":"LOGIC_SET_BUTTON_STATE_ACTION"},{"KEY_STATE_TRUEFALSE":false,"KEY_TYPE":"ON_BUTTON_STATE_CHANGE"},{"KEY_IS_CHANGE_IS_FULL_ICON":false,"kiTF":false,"KEY_START_COLOR":-13421773,"kiTOV":false,"KEY_IS_CHANGE_TITLE":false,"KEY_IS_CHANGE_TEXT_COLOR":false,"KEY_END_COLOR":-16777216,"KEY_IS_CHANGE_ICON":false,"kiBD":false,"KEY_IS_CHANGE_ALIGN_HOR":false,"KEY_IS_CHANGE_IS_ROUNDED":false,"kIEn":true,"kC":false,"kiTOH":false,"KEY_TYPE":"CHANGE_BUTTON_VISUALS_ACTION","KEY_IS_CHANGE_BG_COLOR":true,"KEY_IS_CHANGE_IS_TRANSPARENT":false,"KEY_IS_CHANGE_ALIGN_VERT":false},{"KEY_STATE_TRUEFALSE":true,"KEY_TYPE":"ON_BUTTON_STATE_CHANGE"},{"KEY_IS_CHANGE_IS_FULL_ICON":false,"kiTF":false,"KEY_START_COLOR":-8349185,"kiTOV":false,"KEY_IS_CHANGE_TITLE":false,"KEY_IS_CHANGE_TEXT_COLOR":false,"KEY_END_COLOR":-13414989,"KEY_IS_CHANGE_ICON":false,"kiBD":false,"KEY_IS_CHANGE_ALIGN_HOR":false,"KEY_IS_CHANGE_IS_ROUNDED":false,"kIEn":true,"kC":false,"kiTOH":false,"KEY_TYPE":"CHANGE_BUTTON_VISUALS_ACTION","KEY_IS_CHANGE_BG_COLOR":true,"KEY_IS_CHANGE_IS_TRANSPARENT":false,"KEY_IS_CHANGE_ALIGN_VERT":false}],"kIAPBKC":-14803426,"I":"","ITS":true,"BiR":true,"kSCTY":0,"BiT":false,"kSCHS":false,"inS":"","IiS":false,"T":"Start Stopwatch\n1","kSCAC":-14145496,"kSCC":-4611631,"kSCHRC":false,"THO":4,"id":"u235bme878kln","GUdata":"","kSCIUFATS":false,"kCT":1,"kSIP":0,"TELS":5,"kSCI":"","kIAs":[],"GUid":-1,"kSCIIVA":true,"COLS":1,"TA":5,"TC":-1,"kSVP":0,"kSTP":0,"kSVAC":-10575407,"TO":4,"TP":2,"inB":false,"EXP":[],"kSD":0,"kSCTM":0,"TS":11,"inC":0,"ROWS":1}