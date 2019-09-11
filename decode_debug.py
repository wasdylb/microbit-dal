import sys

# log_start = 85
log_pointer = 106
log = [2972844056, 1072693256, 325189656, 346161152, 2494693664, 1072693256,
  516030752, 531759360, 2680291712, 836895104, 516030848, 579993600,
  2728591365, 780337157, 781189130, 795017217, 2972909577, 1072693256,
  325255177, 373489664, 2522022400, 1072693256, 400753152, 2556625410,
  836960770, 400753154, 2576550402, 836962818, 400755202, 441647618,
  473104898, 479395840, 2628977684, 594740244, 780338196, 781189123,
  795018256, 818086912, 2966619168, 594740256, 623051776, 2771584128,
  2786268288, 650318976, 664994944, 836961408, 594740352, 610467840,
  2759000069, 780337157, 781189130, 795017217, 2972909577, 1072693256,
  325255177, 373489664, 2522022400, 1072693252, 1072693256, 400753152,
  2556625410, 1072693249, 1072693252, 870449172, 780271636, 781189123,
  794951696, 2972844056, 1072693256, 325189656, 346161152, 2494693664,
  1072693256, 516030752, 531759360, 2680291712, 836895104, 516030848,
  579993600, 2728591365, 780337157, 781189130, 795017217, 2972909577,
  1072693256, 325255177, 373489664, 2522022400, 1072693256, 400753152,
  2556625410, 836960770, 400753154, 2576550402, 836962818, 400755202,
  441647618, 473104898, 479395840, 2628977684, 594740244, 780338196,
  781189123, 795018256, 818086912, 2966619168, 795017217, 2972909577,
  1072693256, 325255177, 373489664, 2522022400, 1072693256, 400753152,
  2556625410, 836960770, 400753154, 2576550402, 836962818, 400755202,
  441647618, 1072693252, 870449172, 780271636, 781189123, 794951696,
  2972844056, 1072693256, 325189656, 346161152, 2494693664, 1072693256,
  516030752, 531759360, 2680291712, 836895104, 516030848, 579993600,
  2728591365, 780337157, 781189130, 795017217, 2972909577, 1072693256,
  325255177, 373489664, 2522022400, 1072693256, 400753152, 2556625410,
  836960770, 400753154, 2576550402, 836962818, 400755202, 441647618,
  473104898, 479395840, 2628977684, 594740244, 780338196, 781189123,
  795018256, 818086912, 2966619168, 594740256, 623051776, 2771584128,
  2786268288, 650318976, 664994944, 836961408, 594740352, 610467840,
  2759000069, 780337157, 781189130, 795017217, 2972909577, 1072693256,
  325255177, 373489664, 2522022400, 1072693256, 400753152, 2556625410,
  1072693252, 870449172, 780271636, 781189123, 794951696, 2972844056,
  1072693256, 325189656, 346161152, 2494693664, 1072693256, 516030752,
  531759360, 2680291712, 836895104, 516030848, 579993600, 2728591365,
  780337157, 781189130, 795017217, 2972909577, 1072693256, 325255177,
  373489664, 2522022400, 1072693256, 400753152, 2556625410, 836960770,
  400753154, 2576550402, 836962818, 400755202, 441647618, 473104898,
  479395840, 2628977684, 594740244, 780338196, 781189123, 795018256,
  818086912, 2966619168, 594740256, 623051776, 2771584128, 2786268288,
  650318976, 664994944, 836961408, 594740352, 610467840, 2759000069,
  780337157, 781189130, 795017217, 2972909577, 1072693256, 325255177,
  373489664, 2522022400, 1072693256, 400753152, 2556625410, 1072693249,
  1072693252, 870449172, 780271636, 781189123, 794951696, 2972844056,
  1072693256, 325189656, 346161152, 2494693664, 1072693256, 516030752,
  531759360, 2680291712, 836895104, 516030848, 579993600, 2728591365,
  780337157, 781189130, 795017217, 2972909577, 1072693256, 325255177,
  373489664, 2522022400, 1072693256, 400753152, 2556625410, 836960770,
  400753154, 2576550402, 836962818, 400755202, 441647618, 473104898,
  479395840, 2628977684, 594740244, 780338196, 781189123, 795018256,
  818086912, 2966619168, 594740256, 623051776, 2771584128, 2786268288,
  650318976, 664994944, 836961408, 594740352, 610467840, 2759000069,
  780337157, 781189130, 795017217, 2972909577, 1072693256, 325255177,
  373489664, 2522022400, 1072693256, 400753152, 2556625410, 1072693252,
  870449172, 780271636, 781189123, 794951696, 2972844056, 1072693256,
  325189656, 346161152, 2494693664, 1072693256, 516030752, 531759360,
  2680291712, 836895104, 516030848, 579993600, 2728591365, 780337157,
  781189130, 795017217, 2972909577, 1072693256, 325255177, 373489664,
  2522022400, 1072693256, 400753152, 2556625410, 836960770, 400753154,
  2576550402, 836962818, 400755202, 441647618, 473104898, 479395840,
  2628977684, 594740244, 780338196, 781189123, 795018256, 818086912,
  2966619168, 594740256, 623051776, 2771584128, 2786268288, 650318976,
  664994944, 836961408, 594740352, 610467840, 2759000069, 780337157,
  781189130, 795017217, 2972909577, 1072693256, 325255177, 373489664,
  2522022400, 1072693256, 400753152, 2556625410, 1072693252, 870449172,
  780271636, 781189123, 794951696, 2972844056, 1072693256, 325189656,
  346161152, 2494693664, 1072693256, 516030752, 531759360, 2680291712,
  836895104, 516030848, 579993600, 2728591365, 780337157, 781189130,
  795017217, 2972909577, 1072693256, 325255177, 373489664, 2522022400,
  1072693256, 400753152, 2556625410, 1072693249, 1072693252, 870449172,
  780271636, 781189123, 794951696, 2972844056, 1072693256, 325189656,
  346161152, 2494693664, 1072693256, 516030752, 531759360, 2680291712,
  836895104, 516030848, 579993600, 2728591365, 780337157, 781189130,
  795017217, 2972909577, 1072693256, 325255177, 373489664, 2522022400,
  1072693256, 400753152, 2556625410, 1072693249, 1072693252, 870449172,
  780271636, 781189123, 794951696, 2972844056, 1072693256, 325189656,
  346161152, 2494693664, 1072693256, 516030752, 531759360, 2680291712,
  836895104, 516030848, 579993600, 2728591365, 780337157, 781189130,
  795017217, 2972909577, 1072693256, 325255177, 373489664, 2522022400,
  1072693256, 400753152, 2556625410, 836960770, 400753154, 2576550402,
  836962818, 400755202, 441647618, 473104898, 479395840, 2628977684,
  594740244, 780338196, 781189123, 795018256, 818086912, 2966619168,
  594740256, 623051776, 2771584128, 2786268288, 650318976, 664994944,
  836961408, 594740352, 610467840, 2759000069, 780337157, 781189130,
  795017217, 2972909577, 1072693256, 325255177, 373489664, 2522022400,
  1072693256, 400753152, 2556625410, 1072693252, 870449172, 780271636,
  781189123, 794951696]

def process_flags(num):
    flags = {
        "RADIO_STATUS_RX_EN" : 0x00000001,
        "RADIO_STATUS_RX_RDY" : 0x00000002,

        "RADIO_STATUS_DISABLE" : 0x00000004,
        "RADIO_STATUS_DISABLED" : 0x00000008,

        "RADIO_STATUS_TX_EN" : 0x00000010,
        "RADIO_STATUS_TX_RDY" : 0x00000020,
        "RADIO_STATUS_TX_ST" : 0x00000040,
        "RADIO_STATUS_TX_END" : 0x00000080,

        "RADIO_STATUS_TRANSMIT": 0x00000100,
        "RADIO_STATUS_RECEIVE": 0x00000200,
        "RADIO_STATUS_FORWARD": 0x00000400,
        "RADIO_STATUS_RECEIVING": 0x00000800,
        "RADIO_STATUS_STORE": 0x00001000,
        "RADIO_STATUS_DISCOVERING": 0x00002000,
        "RADIO_STATUS_SLEEPING": 0x00004000,
        "RADIO_STATUS_WAKE_CONFIGURED": 0x00008000,
        "RADIO_STATUS_EXPECT_RESPONSE": 0x00010000,
        "RADIO_STATUS_FIRST_PACKET": 0x00020000,
        "RADIO_STATUS_SAMPLING": 0x00040000,
        "RADIO_STATUS_QUEUE_KEEP_ALIVE": 0x00080000,
    }

    lineno = (num & 0x7FF00000) >> 20
    isSet = num & (1 << 31)
    logflags = num & 0x000FFFFF
    hex_logflags = hex(logflags)

    flag_str = ""

    if len(hex_logflags) == 7:

        if isSet > 0:
            flag_str = "S: "
        else:
            flag_str = "U: "

        flag_str += str(lineno) + " " + hex_logflags + " "
        for flag in flags.keys():
            if flags[flag] & logflags:
                flag_str += flag + " "
    else:
        flag_str = "LOG: "+ str(lineno)+ " " + hex_logflags

    print(flag_str)

iterator = log_pointer + 1
log_end = iterator - 1

if log_end < 0:
    log_end = len(log) + log_end

while iterator != log_end:
    process_flags(log[iterator])
    iterator = (iterator + 1) % len(log)



