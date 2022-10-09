# توليد ارقام الدول عشوائيه
def numbers(self):
    self.countryNomper = 0
    self.comboBox_TAZWED = None
    if self.pushButton_Mahgor.isChecked() and self.pushButton_3SHWAE_Mahgor.isChecked():
        self.country_text = self.comboBox_country_3SHWAE_Mahgor.currentText()
        self.comboBox_COD_namper = self.comboBox_COD_3SHWAE_Mahgor
    if self.pushButton_Mahgor.isChecked() and self.pushButton_TAZWED_Mahgor.isChecked():
        self.country_text = self.comboBox_country_Mahgor_TAZWED.currentText()
        self.comboBox_COD_namper = self.comboBox_COD_Mahgor_TAZWED

    match self.country_text:
        case " Albania ":
            print(" Albania ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("672")
            self.comboBox_COD_namper.addItem("673")
            self.comboBox_COD_namper.addItem("674")
            self.comboBox_COD_namper.addItem("675")
            self.comboBox_COD_namper.addItem("676")
            self.comboBox_COD_namper.addItem("678")
            self.comboBox_COD_namper.addItem("679")
            self.comboBox_COD_namper.addItem("682")
            self.comboBox_COD_namper.addItem("683")
            self.comboBox_COD_namper.addItem("684")
            self.comboBox_COD_namper.addItem("685")
            self.comboBox_COD_namper.addItem("686")
            self.comboBox_COD_namper.addItem("687")
            self.comboBox_COD_namper.addItem("688")
            self.comboBox_COD_namper.addItem("689")
            self.comboBox_COD_namper.addItem("699")
            self.countryNomper = 6

        case " Algeria ":
            print(" Algeria ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("54")
            self.comboBox_COD_namper.addItem("55")
            self.comboBox_COD_namper.addItem("56")
            self.comboBox_COD_namper.addItem("67")
            self.comboBox_COD_namper.addItem("66")
            self.comboBox_COD_namper.addItem("77")
            self.countryNomper = 7

        case " Angola ":
            print(" Angola ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("92")
            self.comboBox_COD_namper.addItem("93")
            self.comboBox_COD_namper.addItem("94")
            self.comboBox_COD_namper.addItem("95")
            self.comboBox_COD_namper.addItem("99")
            self.countryNomper = 7

        case " Argentina ":
            print(" Argentina ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("220215")
            self.comboBox_COD_namper.addItem("922033")
            self.comboBox_COD_namper.addItem("923164")
            self.comboBox_COD_namper.addItem("923244")
            self.comboBox_COD_namper.addItem("924735")
            self.comboBox_COD_namper.addItem("926926")
            self.comboBox_COD_namper.addItem("929929")
            self.countryNomper = 5

        case " Armenia ":
            print(" Armenia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("41")
            self.comboBox_COD_namper.addItem("43")
            self.comboBox_COD_namper.addItem("44")
            self.comboBox_COD_namper.addItem("49")
            self.comboBox_COD_namper.addItem("55")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("88")
            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("93")
            self.comboBox_COD_namper.addItem("94")
            self.comboBox_COD_namper.addItem("95")
            self.comboBox_COD_namper.addItem("96")
            self.comboBox_COD_namper.addItem("97")
            self.comboBox_COD_namper.addItem("98")
            self.comboBox_COD_namper.addItem("99")
            self.countryNomper = 6

        case " Australia ":
            print(" Australia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("443")
            self.comboBox_COD_namper.addItem("453")
            self.comboBox_COD_namper.addItem("463")
            self.comboBox_COD_namper.addItem("473")
            self.comboBox_COD_namper.addItem("483")
            self.comboBox_COD_namper.addItem("493")
            self.countryNomper = 6
        case " Austria ":
            print(" Austria ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("650")
            self.comboBox_COD_namper.addItem("651")
            self.comboBox_COD_namper.addItem("652")
            self.comboBox_COD_namper.addItem("653")
            self.comboBox_COD_namper.addItem("655")
            self.comboBox_COD_namper.addItem("657")
            self.comboBox_COD_namper.addItem("659")
            self.comboBox_COD_namper.addItem("660")
            self.comboBox_COD_namper.addItem("661")
            self.comboBox_COD_namper.addItem("663")
            self.comboBox_COD_namper.addItem("664")
            self.comboBox_COD_namper.addItem("665")
            self.comboBox_COD_namper.addItem("666")
            self.comboBox_COD_namper.addItem("667")
            self.comboBox_COD_namper.addItem("668")
            self.comboBox_COD_namper.addItem("669")
            self.comboBox_COD_namper.addItem("677")
            self.comboBox_COD_namper.addItem("688")
            self.comboBox_COD_namper.addItem("699")
            self.countryNomper = 4
        case " Azerbaijan ":
            print(" Azerbaijan ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("10")
            self.comboBox_COD_namper.addItem("40")
            self.comboBox_COD_namper.addItem("44")
            self.comboBox_COD_namper.addItem("50")
            self.comboBox_COD_namper.addItem("51")
            self.comboBox_COD_namper.addItem("55")
            self.comboBox_COD_namper.addItem("60")
            self.comboBox_COD_namper.addItem("70")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("99")
            self.countryNomper = 7

        case " Bangladesh ":
            print(" Bangladesh ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("11")
            self.comboBox_COD_namper.addItem("13")
            self.comboBox_COD_namper.addItem("14")
            self.comboBox_COD_namper.addItem("15")
            self.comboBox_COD_namper.addItem("17")
            self.comboBox_COD_namper.addItem("18")
            self.comboBox_COD_namper.addItem("19")
            self.countryNomper = 8

        case " Belarus ":
            print(" Belarus ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("255")
            self.comboBox_COD_namper.addItem("256")
            self.comboBox_COD_namper.addItem("257")
            self.comboBox_COD_namper.addItem("259")
            self.comboBox_COD_namper.addItem("291")
            self.comboBox_COD_namper.addItem("292")
            self.comboBox_COD_namper.addItem("293")
            self.comboBox_COD_namper.addItem("294")
            self.comboBox_COD_namper.addItem("295")
            self.comboBox_COD_namper.addItem("296")
            self.comboBox_COD_namper.addItem("297")
            self.comboBox_COD_namper.addItem("298")
            self.comboBox_COD_namper.addItem("299")
            self.comboBox_COD_namper.addItem("333")
            self.comboBox_COD_namper.addItem("444")
            self.countryNomper = 6

        case " Belgium ":
            print(" Belgium ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("45")
            self.comboBox_COD_namper.addItem("46")
            self.comboBox_COD_namper.addItem("47")
            self.comboBox_COD_namper.addItem("48")
            self.comboBox_COD_namper.addItem("49")
            self.countryNomper = 7

        case " Benin ":
            print(" Benin ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("51")
            self.comboBox_COD_namper.addItem("52")
            self.comboBox_COD_namper.addItem("53")
            self.comboBox_COD_namper.addItem("54")
            self.comboBox_COD_namper.addItem("55")
            self.comboBox_COD_namper.addItem("56")
            self.comboBox_COD_namper.addItem("57")
            self.comboBox_COD_namper.addItem("58")
            self.comboBox_COD_namper.addItem("59")
            self.comboBox_COD_namper.addItem("66")
            self.comboBox_COD_namper.addItem("90")
            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("93")
            self.comboBox_COD_namper.addItem("94")
            self.comboBox_COD_namper.addItem("95")
            self.comboBox_COD_namper.addItem("96")
            self.comboBox_COD_namper.addItem("97")
            self.comboBox_COD_namper.addItem("98")
            self.comboBox_COD_namper.addItem("99")
            self.countryNomper = 6

        case " Bolivia, Plurinational State of ":
            print(" Bolivia, Plurinational State of ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("6")
            self.comboBox_COD_namper.addItem("7")
            self.countryNomper = 7

        case " Brazil ":
            print(" Brazil ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("839")
            self.countryNomper = 8

        case " Bulgaria ":
            print(" Bulgaria ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("877")
            self.comboBox_COD_namper.addItem("888")
            self.comboBox_COD_namper.addItem("899")
            self.comboBox_COD_namper.addItem("988")
            self.comboBox_COD_namper.addItem("996")
            self.comboBox_COD_namper.addItem("999")
            self.countryNomper = 7

        case " Burkina Faso ":
            print(" Burkina Faso ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("01 ")
            self.comboBox_COD_namper.addItem("02 ")
            self.comboBox_COD_namper.addItem("03 ")
            self.comboBox_COD_namper.addItem("05 ")
            self.comboBox_COD_namper.addItem("06 ")
            self.comboBox_COD_namper.addItem("07 ")
            self.comboBox_COD_namper.addItem("51 ")
            self.comboBox_COD_namper.addItem("52 ")
            self.comboBox_COD_namper.addItem("53 ")
            self.comboBox_COD_namper.addItem("54 ")
            self.comboBox_COD_namper.addItem("55 ")
            self.comboBox_COD_namper.addItem("56 ")
            self.comboBox_COD_namper.addItem("57 ")
            self.comboBox_COD_namper.addItem("58 ")
            self.comboBox_COD_namper.addItem("66")
            self.comboBox_COD_namper.addItem("77")
            self.countryNomper = 6

        case " Cambodia ":
            print(" Cambodia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("1112")
            self.comboBox_COD_namper.addItem("2248")
            self.comboBox_COD_namper.addItem("3348")
            self.comboBox_COD_namper.addItem("3343")
            self.comboBox_COD_namper.addItem("4448")
            self.comboBox_COD_namper.addItem("7077")
            self.comboBox_COD_namper.addItem("8822")
            self.comboBox_COD_namper.addItem("9099")
            self.countryNomper = 5

        case " Cameroon ":
            print(" Cameroon ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("242")
            self.comboBox_COD_namper.addItem("243")
            self.comboBox_COD_namper.addItem("622")
            self.comboBox_COD_namper.addItem("655")
            self.comboBox_COD_namper.addItem("666")
            self.comboBox_COD_namper.addItem("677")
            self.comboBox_COD_namper.addItem("688")
            self.comboBox_COD_namper.addItem("699")
            self.countryNomper = 6

        case " Canada ":
            print(" Canada ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("204")
            self.comboBox_COD_namper.addItem("250")
            self.comboBox_COD_namper.addItem("263")
            self.comboBox_COD_namper.addItem("306")
            self.comboBox_COD_namper.addItem("343")
            self.comboBox_COD_namper.addItem("403")
            self.comboBox_COD_namper.addItem("450")
            self.comboBox_COD_namper.addItem("468")
            self.comboBox_COD_namper.addItem("474")
            self.comboBox_COD_namper.addItem("506")
            self.comboBox_COD_namper.addItem("548")
            self.comboBox_COD_namper.addItem("579")
            self.comboBox_COD_namper.addItem("604")
            self.comboBox_COD_namper.addItem("613")
            self.comboBox_COD_namper.addItem("639")
            self.comboBox_COD_namper.addItem("742")
            self.comboBox_COD_namper.addItem("778")
            self.comboBox_COD_namper.addItem("819")
            self.comboBox_COD_namper.addItem("825")
            self.comboBox_COD_namper.addItem("873")
            self.comboBox_COD_namper.addItem("807")
            self.comboBox_COD_namper.addItem("900")
            self.comboBox_COD_namper.addItem("206")
            self.comboBox_COD_namper.addItem("209")
            self.comboBox_COD_namper.addItem("360")

            self.countryNomper = 7

        case " Chile ":
            print(" Chile ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("21160")
            self.comboBox_COD_namper.addItem("21962")
            self.comboBox_COD_namper.addItem("21982")
            self.comboBox_COD_namper.addItem("22234")
            self.comboBox_COD_namper.addItem("23314")
            self.comboBox_COD_namper.addItem("23316")
            self.comboBox_COD_namper.addItem("23324")
            self.comboBox_COD_namper.addItem("23352")
            self.comboBox_COD_namper.addItem("23375")
            self.comboBox_COD_namper.addItem("23367")
            self.comboBox_COD_namper.addItem("23600")
            self.comboBox_COD_namper.addItem("26466")
            self.comboBox_COD_namper.addItem("38554")
            self.comboBox_COD_namper.addItem("58790")
            self.comboBox_COD_namper.addItem("65865")
            self.comboBox_COD_namper.addItem("80780")
            self.comboBox_COD_namper.addItem("81234")
            self.comboBox_COD_namper.addItem("93608")
            self.comboBox_COD_namper.addItem("93621")
            self.comboBox_COD_namper.addItem("96913")
            self.comboBox_COD_namper.addItem("96997")
            self.comboBox_COD_namper.addItem("97342")
            self.comboBox_COD_namper.addItem("99142")
            self.comboBox_COD_namper.addItem("99123")
            self.comboBox_COD_namper.addItem("99284")
            self.comboBox_COD_namper.addItem("99267")
            self.comboBox_COD_namper.addItem("96783")
            self.countryNomper = 4

        case " China ":
            print(" China ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("1740")
            self.comboBox_COD_namper.addItem("1663")
            self.comboBox_COD_namper.addItem("1445")
            self.comboBox_COD_namper.addItem("1777")
            self.comboBox_COD_namper.addItem("1044")
            self.countryNomper = 7

        case " Colombia ":
            print(" Colombia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("303332")
            self.comboBox_COD_namper.addItem("312343")
            self.comboBox_COD_namper.addItem("320033")
            self.comboBox_COD_namper.addItem("330034")
            self.comboBox_COD_namper.addItem("333300")
            self.comboBox_COD_namper.addItem("333301")
            self.comboBox_COD_namper.addItem("333300")
            self.comboBox_COD_namper.addItem("333477")
            self.comboBox_COD_namper.addItem("355553")
            self.comboBox_COD_namper.addItem("370003")
            self.comboBox_COD_namper.addItem("910133")
            self.countryNomper = 4

        case " Congo ":
            print(" Congo ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("0240")
            self.comboBox_COD_namper.addItem("0250")
            self.comboBox_COD_namper.addItem("0261")
            self.comboBox_COD_namper.addItem("0266")
            self.comboBox_COD_namper.addItem("0267")

            self.countryNomper = 5

        case " Costa Rica ":
            print(" Costa Rica ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("3005")
            self.comboBox_COD_namper.addItem("5500")
            self.comboBox_COD_namper.addItem("6500")
            self.comboBox_COD_namper.addItem("7500")
            self.comboBox_COD_namper.addItem("8500")

            self.countryNomper = 4

        case " Cote d'Ivoire ":
            print(" Cote d'Ivoire ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("0704")
            self.comboBox_COD_namper.addItem("0705")
            self.comboBox_COD_namper.addItem("0777")
            self.countryNomper = 6

        case " Croatia ":
            print(" Croatia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("90997")
            self.comboBox_COD_namper.addItem("97511")
            self.comboBox_COD_namper.addItem("97577")
            self.comboBox_COD_namper.addItem("97599")
            self.comboBox_COD_namper.addItem("97779")
            self.comboBox_COD_namper.addItem("98887")
            self.countryNomper = 4

        case " Czech Republic ":
            print(" Czech Republic ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("601")
            self.comboBox_COD_namper.addItem("602")
            self.comboBox_COD_namper.addItem("603")
            self.comboBox_COD_namper.addItem("604")
            self.comboBox_COD_namper.addItem("605")
            self.comboBox_COD_namper.addItem("606")
            self.comboBox_COD_namper.addItem("607")
            self.comboBox_COD_namper.addItem("608")
            self.comboBox_COD_namper.addItem("702")
            self.comboBox_COD_namper.addItem("703")
            self.comboBox_COD_namper.addItem("704")
            self.comboBox_COD_namper.addItem("705")
            self.comboBox_COD_namper.addItem("723")
            self.comboBox_COD_namper.addItem("733")
            self.comboBox_COD_namper.addItem("772")
            self.comboBox_COD_namper.addItem("799")
            self.countryNomper = 6

        case " Denmark ":
            print(" Denmark ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("22")
            self.comboBox_COD_namper.addItem("32")
            self.comboBox_COD_namper.addItem("42")
            self.comboBox_COD_namper.addItem("50")
            self.comboBox_COD_namper.addItem("69")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("81")
            self.comboBox_COD_namper.addItem("82")
            self.comboBox_COD_namper.addItem("86")
            self.comboBox_COD_namper.addItem("87")
            self.comboBox_COD_namper.addItem("88")
            self.comboBox_COD_namper.addItem("89")
            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("92")
            self.comboBox_COD_namper.addItem("93")
            self.comboBox_COD_namper.addItem("94")
            self.comboBox_COD_namper.addItem("96")
            self.comboBox_COD_namper.addItem("97")
            self.comboBox_COD_namper.addItem("98")
            self.comboBox_COD_namper.addItem("99")
            self.countryNomper = 6

        case " Dominican Republic ":
            print(" Dominican Republic ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("8091")
            self.comboBox_COD_namper.addItem("8491")
            self.comboBox_COD_namper.addItem("3211")

            self.countryNomper = 6

        case " Ecuador ":
            print(" Ecuador ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("939")
            self.comboBox_COD_namper.addItem("964")
            self.comboBox_COD_namper.addItem("969")
            self.comboBox_COD_namper.addItem("999")
            self.comboBox_COD_namper.addItem("966")

            self.countryNomper = 6

        case " Egypt ":
            print(" Egypt ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("10")
            self.comboBox_COD_namper.addItem("11")
            self.comboBox_COD_namper.addItem("12")
            self.comboBox_COD_namper.addItem("15")
            self.countryNomper = 8
        case " El Salvador ":
            print(" El Salvador ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("6")
            self.comboBox_COD_namper.addItem("7")

            self.countryNomper = 7

        case " Estonia ":
            print(" Estonia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("5")
            self.comboBox_COD_namper.addItem("8")

            self.countryNomper = 7

        case " Ethiopia ":
            print(" Ethiopia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("7001")
            self.comboBox_COD_namper.addItem("701")
            self.comboBox_COD_namper.addItem("702")
            self.comboBox_COD_namper.addItem("703")
            self.comboBox_COD_namper.addItem("704")
            self.comboBox_COD_namper.addItem("705")
            self.comboBox_COD_namper.addItem("706")
            self.comboBox_COD_namper.addItem("707")
            self.comboBox_COD_namper.addItem("708")
            self.comboBox_COD_namper.addItem("709")
            self.comboBox_COD_namper.addItem("710")
            self.comboBox_COD_namper.addItem("711")
            self.comboBox_COD_namper.addItem("777")
            self.comboBox_COD_namper.addItem("786")
            self.comboBox_COD_namper.addItem("799")
            self.comboBox_COD_namper.addItem("998")
            self.countryNomper = 6

        case " Finland ":
            print(" Finland ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("4 0")
            self.comboBox_COD_namper.addItem("41")
            self.comboBox_COD_namper.addItem("42")
            self.comboBox_COD_namper.addItem("43")
            self.comboBox_COD_namper.addItem("44")
            self.comboBox_COD_namper.addItem("45")
            self.comboBox_COD_namper.addItem("46")
            self.comboBox_COD_namper.addItem("47")
            self.comboBox_COD_namper.addItem("48")
            self.comboBox_COD_namper.addItem("50")

            self.countryNomper = 4

        case " France ":
            print(" France ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("601")
            self.comboBox_COD_namper.addItem("622")
            self.comboBox_COD_namper.addItem("630")
            self.comboBox_COD_namper.addItem("631")
            self.comboBox_COD_namper.addItem("632")
            self.comboBox_COD_namper.addItem("633")
            self.comboBox_COD_namper.addItem("634")
            self.comboBox_COD_namper.addItem("635")
            self.comboBox_COD_namper.addItem("636")
            self.comboBox_COD_namper.addItem("637")
            self.comboBox_COD_namper.addItem("638")
            self.comboBox_COD_namper.addItem("641")
            self.comboBox_COD_namper.addItem("655")
            self.comboBox_COD_namper.addItem("666")
            self.comboBox_COD_namper.addItem("677")
            self.comboBox_COD_namper.addItem("688")
            self.comboBox_COD_namper.addItem("695")
            self.comboBox_COD_namper.addItem("698")
            self.comboBox_COD_namper.addItem("699")
            self.comboBox_COD_namper.addItem("733")
            self.comboBox_COD_namper.addItem("744")
            self.comboBox_COD_namper.addItem("755")
            self.comboBox_COD_namper.addItem("766")
            self.comboBox_COD_namper.addItem("777")
            self.comboBox_COD_namper.addItem("788")
            self.comboBox_COD_namper.addItem("799")

            self.countryNomper = 6

        case " Gabon ":
            print(" Gabon ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("010")
            self.comboBox_COD_namper.addItem("601")
            self.comboBox_COD_namper.addItem("610")
            self.comboBox_COD_namper.addItem("676")
            self.comboBox_COD_namper.addItem("773")

            self.countryNomper = 5

        case " Germany ":
            print(" Germany ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("15 0")
            self.comboBox_COD_namper.addItem("15 1")
            self.comboBox_COD_namper.addItem("152")
            self.comboBox_COD_namper.addItem("155")
            self.comboBox_COD_namper.addItem("156")
            self.comboBox_COD_namper.addItem("157")
            self.comboBox_COD_namper.addItem("158")
            self.comboBox_COD_namper.addItem("159")

            self.countryNomper = 8
        case " Ghana ":
            print(" Ghana ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("5")
            self.comboBox_COD_namper.addItem("2")

            self.countryNomper = 7

        case " Greece ":
            print(" Greece ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("685")
            self.comboBox_COD_namper.addItem("687")
            self.comboBox_COD_namper.addItem("688")
            self.comboBox_COD_namper.addItem("689")
            self.comboBox_COD_namper.addItem("699")
            self.comboBox_COD_namper.addItem("944")

            self.countryNomper = 6

        case " Guinea ":
            print(" Guinea ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("60")
            self.comboBox_COD_namper.addItem("61")
            self.comboBox_COD_namper.addItem("62")
            self.comboBox_COD_namper.addItem("63")
            self.comboBox_COD_namper.addItem("65")
            self.comboBox_COD_namper.addItem("66")

            self.countryNomper = 7

        case " Haiti ":
            print(" Haiti ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("3")
            self.comboBox_COD_namper.addItem("4")

            self.countryNomper = 7

        case " Honduras ":
            print(" Honduras ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("34")
            self.comboBox_COD_namper.addItem("74")
            self.comboBox_COD_namper.addItem("84")
            self.comboBox_COD_namper.addItem("94")

            self.countryNomper = 6

        case " Hong Kong ":
            print(" Hong Kong ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("44")
            self.comboBox_COD_namper.addItem("46")
            self.comboBox_COD_namper.addItem("56")
            self.comboBox_COD_namper.addItem("57")
            self.comboBox_COD_namper.addItem("60")
            self.comboBox_COD_namper.addItem("67")
            self.comboBox_COD_namper.addItem("84")
            self.comboBox_COD_namper.addItem("90")
            self.comboBox_COD_namper.addItem("91")

            self.countryNomper = 6

        case " Hungary ":
            print(" Hungary ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("20")
            self.comboBox_COD_namper.addItem("30")
            self.comboBox_COD_namper.addItem("31")
            self.comboBox_COD_namper.addItem("50")
            self.comboBox_COD_namper.addItem("70")

            self.countryNomper = 7

        case " India ":
            print(" India ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("61")
            self.comboBox_COD_namper.addItem("62")
            self.comboBox_COD_namper.addItem("63")
            self.comboBox_COD_namper.addItem("64")
            self.comboBox_COD_namper.addItem("65")
            self.comboBox_COD_namper.addItem("66")
            self.comboBox_COD_namper.addItem("67")
            self.comboBox_COD_namper.addItem("68")
            self.comboBox_COD_namper.addItem("70")
            self.comboBox_COD_namper.addItem("71")
            self.comboBox_COD_namper.addItem("72")
            self.comboBox_COD_namper.addItem("73")
            self.comboBox_COD_namper.addItem("74")
            self.comboBox_COD_namper.addItem("75")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("78")
            self.comboBox_COD_namper.addItem("79")
            self.comboBox_COD_namper.addItem("80")
            self.comboBox_COD_namper.addItem("82")
            self.comboBox_COD_namper.addItem("83")
            self.comboBox_COD_namper.addItem("86")
            self.comboBox_COD_namper.addItem("87")
            self.comboBox_COD_namper.addItem("89")
            self.comboBox_COD_namper.addItem("91")
            self.countryNomper = 8

        case " Indonesia ":
            print(" Indonesia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("81")
            self.comboBox_COD_namper.addItem("82")
            self.comboBox_COD_namper.addItem("83")
            self.comboBox_COD_namper.addItem("85")
            self.comboBox_COD_namper.addItem("86")
            self.comboBox_COD_namper.addItem("87")
            self.comboBox_COD_namper.addItem("88")
            self.comboBox_COD_namper.addItem("89")

            self.countryNomper = 7

        case " Iraq ":
            print(" Iraq ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("73")
            self.comboBox_COD_namper.addItem("74")
            self.comboBox_COD_namper.addItem("75")
            self.comboBox_COD_namper.addItem("76")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("78")
            self.comboBox_COD_namper.addItem("79")

            self.countryNomper = 8

        case " Ireland ":
            print(" Ireland ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("83")
            self.comboBox_COD_namper.addItem("85")
            self.comboBox_COD_namper.addItem("86")
            self.comboBox_COD_namper.addItem("87")
            self.comboBox_COD_namper.addItem("88")
            self.comboBox_COD_namper.addItem("89")

            self.countryNomper = 7

        case " Israel ":
            print(" Israel ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("54")

            self.countryNomper = 7

        case " Italy ":
            print(" Italy ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("31")
            self.comboBox_COD_namper.addItem("32")
            self.comboBox_COD_namper.addItem("33")
            self.comboBox_COD_namper.addItem("34")
            self.comboBox_COD_namper.addItem("35")
            self.comboBox_COD_namper.addItem("36")
            self.comboBox_COD_namper.addItem("37")
            self.comboBox_COD_namper.addItem("38")
            self.comboBox_COD_namper.addItem("39")

            self.countryNomper = 8

        case " Jamaica ":
            print(" Jamaica ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("87620")
            self.comboBox_COD_namper.addItem("87622")
            self.comboBox_COD_namper.addItem("87623")
            self.comboBox_COD_namper.addItem("87650")
            self.comboBox_COD_namper.addItem("87655")
            self.comboBox_COD_namper.addItem("87664")
            self.comboBox_COD_namper.addItem("87666")
            self.comboBox_COD_namper.addItem("87670")
            self.comboBox_COD_namper.addItem("87677")
            self.comboBox_COD_namper.addItem("87678")
            self.comboBox_COD_namper.addItem("87679")
            self.comboBox_COD_namper.addItem("87699")
            self.comboBox_COD_namper.addItem("87687")

            self.countryNomper = 5

        case " Japan ":
            print(" Japan ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("001")

            self.countryNomper = 7

        case " Jordan ":
            print(" Jordan ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("770")
            self.comboBox_COD_namper.addItem("771")
            self.comboBox_COD_namper.addItem("772")
            self.comboBox_COD_namper.addItem("775")
            self.comboBox_COD_namper.addItem("776")
            self.comboBox_COD_namper.addItem("777")
            self.comboBox_COD_namper.addItem("778")
            self.comboBox_COD_namper.addItem("779")
            self.comboBox_COD_namper.addItem("781")
            self.comboBox_COD_namper.addItem("782")
            self.comboBox_COD_namper.addItem("785")
            self.comboBox_COD_namper.addItem("786")
            self.comboBox_COD_namper.addItem("787")
            self.comboBox_COD_namper.addItem("788")
            self.comboBox_COD_namper.addItem("789")
            self.comboBox_COD_namper.addItem("790")
            self.countryNomper = 6

        case " Kazakhstan ":
            print(" Kazakhstan ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("700")
            self.comboBox_COD_namper.addItem("701")
            self.comboBox_COD_namper.addItem("702")
            self.comboBox_COD_namper.addItem("703")
            self.comboBox_COD_namper.addItem("704")
            self.comboBox_COD_namper.addItem("705")
            self.comboBox_COD_namper.addItem("706")
            self.comboBox_COD_namper.addItem("707")
            self.comboBox_COD_namper.addItem("708")
            self.comboBox_COD_namper.addItem("747")
            self.comboBox_COD_namper.addItem("760")
            self.comboBox_COD_namper.addItem("761")
            self.comboBox_COD_namper.addItem("762")
            self.comboBox_COD_namper.addItem("763")
            self.comboBox_COD_namper.addItem("764")
            self.comboBox_COD_namper.addItem("771")
            self.comboBox_COD_namper.addItem("775")
            self.comboBox_COD_namper.addItem("776")
            self.comboBox_COD_namper.addItem("777")
            self.comboBox_COD_namper.addItem("778")
            self.comboBox_COD_namper.addItem("785")
            self.countryNomper = 7

        case " Kyrgyzstan ":
            print(" Kyrgyzstan ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("20")
            self.comboBox_COD_namper.addItem("22")
            self.comboBox_COD_namper.addItem("55")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("88")
            self.comboBox_COD_namper.addItem("99")

            self.countryNomper = 7

        case " Latvia ":
            print(" Latvia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("2323")
            self.comboBox_COD_namper.addItem("2333")

            self.countryNomper = 4

        case " Lebanon ":
            print(" Lebanon ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("76")
            self.comboBox_COD_namper.addItem("78")
            self.comboBox_COD_namper.addItem("79")
            self.comboBox_COD_namper.addItem("81")
            self.comboBox_COD_namper.addItem("3")

            self.countryNomper = 6

        case " Liberia ":
            print(" Liberia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("88")

            self.countryNomper = 7

        case " Libya ":
            print(" Libya ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("92")
            self.comboBox_COD_namper.addItem("93")
            self.comboBox_COD_namper.addItem("94")
            self.comboBox_COD_namper.addItem("95")
            self.comboBox_COD_namper.addItem("96")

            self.countryNomper = 7

        case " Lithuania ":
            print(" Lithuania ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("6")

            self.countryNomper = 7

        case " Luxembourg ":
            print(" Luxembourg ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("621")
            self.comboBox_COD_namper.addItem("628")
            self.comboBox_COD_namper.addItem("651")
            self.comboBox_COD_namper.addItem("655")
            self.comboBox_COD_namper.addItem("656")
            self.comboBox_COD_namper.addItem("658")
            self.comboBox_COD_namper.addItem("661")
            self.comboBox_COD_namper.addItem("668")
            self.comboBox_COD_namper.addItem("671")
            self.comboBox_COD_namper.addItem("678")
            self.comboBox_COD_namper.addItem("679")
            self.comboBox_COD_namper.addItem("681")
            self.comboBox_COD_namper.addItem("691")
            self.comboBox_COD_namper.addItem("698")

            self.countryNomper = 6

        case " North Macedonia ":
            print(" North Macedonia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("737")
            self.comboBox_COD_namper.addItem("74 2")
            self.comboBox_COD_namper.addItem("74 7")
            self.comboBox_COD_namper.addItem("79 4")
            self.comboBox_COD_namper.addItem("79 7")
            self.countryNomper = 5

        case " Madagascar ":
            print(" Madagascar ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("32")
            self.comboBox_COD_namper.addItem("33")
            self.comboBox_COD_namper.addItem("34")
            self.comboBox_COD_namper.addItem("38")
            self.comboBox_COD_namper.addItem("39")

            self.countryNomper = 7

        case " Malawi ":
            print(" Malawi ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("111")
            self.comboBox_COD_namper.addItem("988")
            self.comboBox_COD_namper.addItem("999")

            self.countryNomper = 6

        case " Malaysia ":
            print(" Malaysia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("104")
            self.comboBox_COD_namper.addItem("107")
            self.comboBox_COD_namper.addItem("109")
            self.comboBox_COD_namper.addItem("144")
            self.comboBox_COD_namper.addItem("185")
            self.comboBox_COD_namper.addItem("187")
            self.comboBox_COD_namper.addItem("188")
            self.comboBox_COD_namper.addItem("189")

            self.countryNomper = 5

        case " Mauritius ":
            print(" Mauritius ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("542")
            self.comboBox_COD_namper.addItem("547")
            self.comboBox_COD_namper.addItem("587")
            self.comboBox_COD_namper.addItem("597")
            self.comboBox_COD_namper.addItem("527")
            self.comboBox_COD_namper.addItem("522")

            self.countryNomper = 5

        case " Mexico ":
            print(" Mexico ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("222")
            self.comboBox_COD_namper.addItem("123")
            self.comboBox_COD_namper.addItem("124")
            self.comboBox_COD_namper.addItem("127")
            self.comboBox_COD_namper.addItem("128")
            self.comboBox_COD_namper.addItem("129")
            self.comboBox_COD_namper.addItem("131")
            self.comboBox_COD_namper.addItem("133")
            self.comboBox_COD_namper.addItem("137")
            self.comboBox_COD_namper.addItem("139")
            self.comboBox_COD_namper.addItem("133")
            self.comboBox_COD_namper.addItem("141")
            self.comboBox_COD_namper.addItem("143")
            self.comboBox_COD_namper.addItem("148")
            self.comboBox_COD_namper.addItem("149")
            self.comboBox_COD_namper.addItem("144")
            self.comboBox_COD_namper.addItem("158")
            self.comboBox_COD_namper.addItem("159")
            self.comboBox_COD_namper.addItem("155")
            self.comboBox_COD_namper.addItem("161")
            self.comboBox_COD_namper.addItem("165")
            self.comboBox_COD_namper.addItem("166")
            self.comboBox_COD_namper.addItem("167")
            self.comboBox_COD_namper.addItem("168")
            self.comboBox_COD_namper.addItem("169")
            self.comboBox_COD_namper.addItem("166")
            self.comboBox_COD_namper.addItem("175")
            self.comboBox_COD_namper.addItem("178")
            self.comboBox_COD_namper.addItem("179")
            self.comboBox_COD_namper.addItem("177")
            self.comboBox_COD_namper.addItem("181")
            self.comboBox_COD_namper.addItem("182")
            self.comboBox_COD_namper.addItem("183")
            self.comboBox_COD_namper.addItem("184")
            self.comboBox_COD_namper.addItem("186")
            self.comboBox_COD_namper.addItem("187")
            self.comboBox_COD_namper.addItem("189")
            self.comboBox_COD_namper.addItem("191")
            self.comboBox_COD_namper.addItem("192")
            self.comboBox_COD_namper.addItem("193")
            self.comboBox_COD_namper.addItem("195")
            self.comboBox_COD_namper.addItem("197")
            self.comboBox_COD_namper.addItem("198")
            self.comboBox_COD_namper.addItem("199")
            self.comboBox_COD_namper.addItem("233")
            self.comboBox_COD_namper.addItem("244")
            self.comboBox_COD_namper.addItem("277")
            self.comboBox_COD_namper.addItem("288")
            self.comboBox_COD_namper.addItem("299")
            self.comboBox_COD_namper.addItem("311")
            self.comboBox_COD_namper.addItem("333")
            self.comboBox_COD_namper.addItem("377")
            self.comboBox_COD_namper.addItem("399")
            self.comboBox_COD_namper.addItem("333")
            self.comboBox_COD_namper.addItem("411")
            self.comboBox_COD_namper.addItem("433")
            self.comboBox_COD_namper.addItem("444")
            self.comboBox_COD_namper.addItem("488")
            self.comboBox_COD_namper.addItem("499")
            self.comboBox_COD_namper.addItem("588")
            self.comboBox_COD_namper.addItem("599")
            self.comboBox_COD_namper.addItem("555")
            self.comboBox_COD_namper.addItem("611")
            self.comboBox_COD_namper.addItem("657")
            self.comboBox_COD_namper.addItem("655")
            self.comboBox_COD_namper.addItem("666")
            self.comboBox_COD_namper.addItem("677")
            self.comboBox_COD_namper.addItem("688")
            self.comboBox_COD_namper.addItem("699")
            self.comboBox_COD_namper.addItem("755")
            self.comboBox_COD_namper.addItem("788")
            self.comboBox_COD_namper.addItem("799")
            self.comboBox_COD_namper.addItem("777")
            self.comboBox_COD_namper.addItem("811")
            self.comboBox_COD_namper.addItem("822")
            self.comboBox_COD_namper.addItem("833")
            self.comboBox_COD_namper.addItem("844")
            self.comboBox_COD_namper.addItem("866")
            self.comboBox_COD_namper.addItem("877")
            self.comboBox_COD_namper.addItem("899")
            self.comboBox_COD_namper.addItem("911")
            self.comboBox_COD_namper.addItem("922")
            self.comboBox_COD_namper.addItem("933")
            self.comboBox_COD_namper.addItem("955")
            self.comboBox_COD_namper.addItem("966")
            self.comboBox_COD_namper.addItem("977")
            self.comboBox_COD_namper.addItem("988")
            self.comboBox_COD_namper.addItem("999")

            self.countryNomper = 8

        case " Moldova ":
            print(" Moldova ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("562")
            self.comboBox_COD_namper.addItem("712")
            self.comboBox_COD_namper.addItem("762")
            self.comboBox_COD_namper.addItem("772")
            self.comboBox_COD_namper.addItem("782")
            self.comboBox_COD_namper.addItem("792")

            self.countryNomper = 5
        case " Mongolia ":
            print(" Mongolia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("920")
            self.comboBox_COD_namper.addItem("833")
            self.comboBox_COD_namper.addItem("661")
            self.comboBox_COD_namper.addItem("525")

            self.countryNomper = 5

        case " Morocco ":
            print(" Morocco ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("رقم الشبكه غير معروف")

            self.countryNomper = 6

        case " Mozambique ":
            print(" Mozambique ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("82")
            self.comboBox_COD_namper.addItem("83")
            self.comboBox_COD_namper.addItem("84")
            self.comboBox_COD_namper.addItem("85")
            self.comboBox_COD_namper.addItem("867")
            self.comboBox_COD_namper.addItem("89")

            self.countryNomper = 7

        case " Nepal ":
            print(" Nepal ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("960")
            self.comboBox_COD_namper.addItem("961")
            self.comboBox_COD_namper.addItem("962")
            self.comboBox_COD_namper.addItem("963")
            self.comboBox_COD_namper.addItem("970")
            self.comboBox_COD_namper.addItem("972")
            self.comboBox_COD_namper.addItem("974")
            self.comboBox_COD_namper.addItem("975")
            self.comboBox_COD_namper.addItem("976")
            self.comboBox_COD_namper.addItem("980")
            self.comboBox_COD_namper.addItem("981")
            self.comboBox_COD_namper.addItem("982")
            self.comboBox_COD_namper.addItem("984")
            self.comboBox_COD_namper.addItem("985")
            self.comboBox_COD_namper.addItem("986")
            self.comboBox_COD_namper.addItem("988")

            self.countryNomper = 7

        case " Netherlands ":
            print(" Netherlands ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("610")
            self.comboBox_COD_namper.addItem("620")
            self.comboBox_COD_namper.addItem("630")
            self.comboBox_COD_namper.addItem("640")
            self.comboBox_COD_namper.addItem("650")
            self.comboBox_COD_namper.addItem("680")

            self.countryNomper = 6

        case " New Zealand ":
            print(" New Zealand ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("20")
            self.comboBox_COD_namper.addItem("21")
            self.comboBox_COD_namper.addItem("22")
            self.comboBox_COD_namper.addItem("27")
            self.comboBox_COD_namper.addItem("28")
            self.comboBox_COD_namper.addItem("29")

            self.countryNomper = 7

        case " Nicaragua ":
            print(" Nicaragua ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("620")
            self.comboBox_COD_namper.addItem("555")
            self.comboBox_COD_namper.addItem("633")
            self.comboBox_COD_namper.addItem("644")
            self.comboBox_COD_namper.addItem("655")
            self.comboBox_COD_namper.addItem("677")
            self.comboBox_COD_namper.addItem("688")
            self.comboBox_COD_namper.addItem("699")
            self.comboBox_COD_namper.addItem("711")
            self.comboBox_COD_namper.addItem("811")

            self.countryNomper = 5

        case " Nigeria ":
            print(" Nigeria ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("801")
            self.comboBox_COD_namper.addItem("819")
            self.comboBox_COD_namper.addItem("810")
            self.comboBox_COD_namper.addItem("900")
            self.comboBox_COD_namper.addItem("910")

            self.countryNomper = 7
        case " Norway ":
            print(" Norway ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("40")
            self.comboBox_COD_namper.addItem("41")
            self.comboBox_COD_namper.addItem("45")
            self.comboBox_COD_namper.addItem("46")
            self.comboBox_COD_namper.addItem("47")
            self.comboBox_COD_namper.addItem("48")
            self.comboBox_COD_namper.addItem("59")
            self.comboBox_COD_namper.addItem("91")

            self.countryNomper = 6

        case " Oman ":
            print(" Oman ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("1505")
            self.comboBox_COD_namper.addItem("7705")
            self.comboBox_COD_namper.addItem("9003")

            self.countryNomper = 4

        case " Pakistan ":
            print(" Pakistan ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("301")
            self.comboBox_COD_namper.addItem("313")
            self.comboBox_COD_namper.addItem("323")
            self.comboBox_COD_namper.addItem("330")
            self.comboBox_COD_namper.addItem("331")
            self.comboBox_COD_namper.addItem("332")
            self.comboBox_COD_namper.addItem("333")
            self.comboBox_COD_namper.addItem("334")
            self.comboBox_COD_namper.addItem("335")
            self.comboBox_COD_namper.addItem("336")
            self.comboBox_COD_namper.addItem("337")
            self.comboBox_COD_namper.addItem("343")
            self.comboBox_COD_namper.addItem("355")
            self.comboBox_COD_namper.addItem("364")

            self.countryNomper = 7

        case " Paraguay ":
            print(" Paraguay ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("961")
            self.comboBox_COD_namper.addItem("962")
            self.comboBox_COD_namper.addItem("969")
            self.comboBox_COD_namper.addItem("971")
            self.comboBox_COD_namper.addItem("972")
            self.comboBox_COD_namper.addItem("973")
            self.comboBox_COD_namper.addItem("974")
            self.comboBox_COD_namper.addItem("975")
            self.comboBox_COD_namper.addItem("976")
            self.comboBox_COD_namper.addItem("981")
            self.comboBox_COD_namper.addItem("982")
            self.comboBox_COD_namper.addItem("983")
            self.comboBox_COD_namper.addItem("984")
            self.comboBox_COD_namper.addItem("985")
            self.comboBox_COD_namper.addItem("986")
            self.comboBox_COD_namper.addItem("991")
            self.comboBox_COD_namper.addItem("992")
            self.comboBox_COD_namper.addItem("993")
            self.comboBox_COD_namper.addItem("994")
            self.comboBox_COD_namper.addItem("995")

            self.countryNomper = 6

        case " Peru ":
            print(" Peru ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.comboBox_COD_namper.addItem("")
            self.countryNomper = 6

        case " Philippines ":
            print(" Philippines ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("81")
            self.comboBox_COD_namper.addItem("89")
            self.comboBox_COD_namper.addItem("90")
            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("94")
            self.comboBox_COD_namper.addItem("98")
            self.comboBox_COD_namper.addItem("99")

            self.countryNomper = 8

        case " Poland ":
            print(" Poland ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("2113")
            self.comboBox_COD_namper.addItem("2111")
            self.comboBox_COD_namper.addItem("2122")
            self.comboBox_COD_namper.addItem("4556")
            self.comboBox_COD_namper.addItem("5645")
            self.comboBox_COD_namper.addItem("6623")
            self.comboBox_COD_namper.addItem("7623")
            self.comboBox_COD_namper.addItem("8885")

            self.countryNomper = 5

        case " Portugal ":
            print(" Portugal ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("9")

            self.countryNomper = 8

        case " Qatar ":
            print(" Qatar ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("28")
            self.comboBox_COD_namper.addItem("29")
            self.comboBox_COD_namper.addItem("30")
            self.comboBox_COD_namper.addItem("50")
            self.comboBox_COD_namper.addItem("60")
            self.comboBox_COD_namper.addItem("70")

            self.countryNomper = 6

        case " Romania ":
            print(" Romania ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("70 ")
            self.comboBox_COD_namper.addItem("71")
            self.comboBox_COD_namper.addItem("72")
            self.comboBox_COD_namper.addItem("73")
            self.comboBox_COD_namper.addItem("74")
            self.comboBox_COD_namper.addItem("75")
            self.comboBox_COD_namper.addItem("76")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("78")
            self.comboBox_COD_namper.addItem("79")

            self.countryNomper = 7

        case " Russian Federation ":
            print(" Russian Federation ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("9")

            self.countryNomper = 9

        case " Saudi Arabia ":
            print(" Saudi Arabia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("50")
            self.comboBox_COD_namper.addItem("51")
            self.comboBox_COD_namper.addItem("53")
            self.comboBox_COD_namper.addItem("54")
            self.comboBox_COD_namper.addItem("55")
            self.comboBox_COD_namper.addItem("56")
            self.comboBox_COD_namper.addItem("58")
            self.comboBox_COD_namper.addItem("59")

            self.countryNomper = 7

        case " Senegal ":
            print(" Senegal ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("70")
            self.comboBox_COD_namper.addItem("76")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("78")

            self.countryNomper = 7

        case " Singapore ":
            print(" Singapore ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("8")
            self.comboBox_COD_namper.addItem("9")

            self.countryNomper = 7

        case " Slovakia ":
            print(" Slovakia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("90")
            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("94")
            self.comboBox_COD_namper.addItem("95")
            self.comboBox_COD_namper.addItem("9")

            self.countryNomper = 7

        case " Slovenia ":
            print(" Slovenia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("51")
            self.comboBox_COD_namper.addItem("41")
            self.comboBox_COD_namper.addItem("61")

            self.countryNomper = 6

        case " Somalia ":
            print(" Somalia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("3")
            self.comboBox_COD_namper.addItem("4")
            self.comboBox_COD_namper.addItem("6")
            self.comboBox_COD_namper.addItem("8")

            self.countryNomper = 8

        case " South Africa ":
            print(" South Africa ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("69")
            self.comboBox_COD_namper.addItem("79")
            self.comboBox_COD_namper.addItem("19")

            self.countryNomper = 7

        case " Spain ":
            print(" Spain ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("6")
            self.comboBox_COD_namper.addItem("7")

            self.countryNomper = 8

        case " Sweden ":
            print(" Sweden ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("70")
            self.comboBox_COD_namper.addItem("72")
            self.comboBox_COD_namper.addItem("73")
            self.comboBox_COD_namper.addItem("76")
            self.comboBox_COD_namper.addItem("79")

            self.countryNomper = 7

        case " Switzerland ":
            print(" Switzerland ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("73")
            self.comboBox_COD_namper.addItem("75")
            self.comboBox_COD_namper.addItem("76")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("78")
            self.comboBox_COD_namper.addItem("79")

            self.countryNomper = 7

        case " Tanzania, United Republic of ":
            print(" Tanzania, United Republic of ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("610")
            self.comboBox_COD_namper.addItem("620")
            self.comboBox_COD_namper.addItem("650")
            self.comboBox_COD_namper.addItem("660")
            self.comboBox_COD_namper.addItem("677")
            self.comboBox_COD_namper.addItem("688")
            self.comboBox_COD_namper.addItem("699")
            self.comboBox_COD_namper.addItem("711")
            self.comboBox_COD_namper.addItem("733")
            self.comboBox_COD_namper.addItem("744")
            self.comboBox_COD_namper.addItem("755")
            self.comboBox_COD_namper.addItem("766")
            self.comboBox_COD_namper.addItem("772")
            self.comboBox_COD_namper.addItem("773")
            self.comboBox_COD_namper.addItem("774")
            self.comboBox_COD_namper.addItem("775")
            self.comboBox_COD_namper.addItem("776")
            self.comboBox_COD_namper.addItem("777")
            self.comboBox_COD_namper.addItem("778")
            self.comboBox_COD_namper.addItem("779")
            self.comboBox_COD_namper.addItem("780")
            self.comboBox_COD_namper.addItem("790")

            self.countryNomper = 6

        case " Thailand ":
            print(" Thailand ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("61")
            self.comboBox_COD_namper.addItem("62")
            self.comboBox_COD_namper.addItem("63")
            self.comboBox_COD_namper.addItem("64")
            self.comboBox_COD_namper.addItem("65")
            self.comboBox_COD_namper.addItem("66")
            self.comboBox_COD_namper.addItem("81")
            self.comboBox_COD_namper.addItem("91")

            self.countryNomper = 7

        case " Togo ":
            print(" Togo ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("70")
            self.comboBox_COD_namper.addItem("79")
            self.comboBox_COD_namper.addItem("90")
            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("92")
            self.comboBox_COD_namper.addItem("93")
            self.comboBox_COD_namper.addItem("96")
            self.comboBox_COD_namper.addItem("97")
            self.comboBox_COD_namper.addItem("98")
            self.comboBox_COD_namper.addItem("99")

            self.countryNomper = 6

        case " Tunisia ":
            print(" Tunisia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("31")
            self.comboBox_COD_namper.addItem("36")
            self.comboBox_COD_namper.addItem("40")

            self.countryNomper = 6

        case " Turkey ":
            print(" Turkey ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("50")
            self.comboBox_COD_namper.addItem("51")
            self.comboBox_COD_namper.addItem("55")
            self.comboBox_COD_namper.addItem("59")

            self.countryNomper = 8

        case " Uganda ":
            print(" Uganda ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("720")
            self.comboBox_COD_namper.addItem("726")
            self.comboBox_COD_namper.addItem("736")
            self.comboBox_COD_namper.addItem("790")

            self.countryNomper = 6

        case " Ukraine ":
            print(" Ukraine ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("63")
            self.comboBox_COD_namper.addItem("66")
            self.comboBox_COD_namper.addItem("67")
            self.comboBox_COD_namper.addItem("68")
            self.comboBox_COD_namper.addItem("71")
            self.comboBox_COD_namper.addItem("72")
            self.comboBox_COD_namper.addItem("73")
            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("92")
            self.comboBox_COD_namper.addItem("93")
            self.comboBox_COD_namper.addItem("94")
            self.comboBox_COD_namper.addItem("95")
            self.comboBox_COD_namper.addItem("96")
            self.comboBox_COD_namper.addItem("97")
            self.comboBox_COD_namper.addItem("98")
            self.comboBox_COD_namper.addItem("99")

            self.countryNomper = 7

        case " United Arab Emirates ":
            print(" United Arab Emirates ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("50")
            self.comboBox_COD_namper.addItem("52")
            self.comboBox_COD_namper.addItem("54")
            self.comboBox_COD_namper.addItem("55")
            self.comboBox_COD_namper.addItem("56")
            self.comboBox_COD_namper.addItem("58")

            self.countryNomper = 7

        case " United Kingdom ":
            print(" United Kingdom ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("74")
            self.comboBox_COD_namper.addItem("75")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("78")
            self.comboBox_COD_namper.addItem("79")

            self.countryNomper = 8

        case " United States ":
            print(" United States ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("20")
            self.comboBox_COD_namper.addItem("21")
            self.comboBox_COD_namper.addItem("22")
            self.comboBox_COD_namper.addItem("23")
            self.comboBox_COD_namper.addItem("24")
            self.comboBox_COD_namper.addItem("25")
            self.comboBox_COD_namper.addItem("26")
            self.comboBox_COD_namper.addItem("27")
            self.comboBox_COD_namper.addItem("28")
            self.comboBox_COD_namper.addItem("30")
            self.comboBox_COD_namper.addItem("31")
            self.comboBox_COD_namper.addItem("32")
            self.comboBox_COD_namper.addItem("33")
            self.comboBox_COD_namper.addItem("34")
            self.comboBox_COD_namper.addItem("35")
            self.comboBox_COD_namper.addItem("36")
            self.comboBox_COD_namper.addItem("38")
            self.comboBox_COD_namper.addItem("40")
            self.comboBox_COD_namper.addItem("41")
            self.comboBox_COD_namper.addItem("42")
            self.comboBox_COD_namper.addItem("43")
            self.comboBox_COD_namper.addItem("44")
            self.comboBox_COD_namper.addItem("46")
            self.comboBox_COD_namper.addItem("47")
            self.comboBox_COD_namper.addItem("48")
            self.comboBox_COD_namper.addItem("50")
            self.comboBox_COD_namper.addItem("51")
            self.comboBox_COD_namper.addItem("53")
            self.comboBox_COD_namper.addItem("54")
            self.comboBox_COD_namper.addItem("55")
            self.comboBox_COD_namper.addItem("56")
            self.comboBox_COD_namper.addItem("57")
            self.comboBox_COD_namper.addItem("58")
            self.comboBox_COD_namper.addItem("60")
            self.comboBox_COD_namper.addItem("61")
            self.comboBox_COD_namper.addItem("62")
            self.comboBox_COD_namper.addItem("65")
            self.comboBox_COD_namper.addItem("66")
            self.comboBox_COD_namper.addItem("68")
            self.comboBox_COD_namper.addItem("70")
            self.comboBox_COD_namper.addItem("71")
            self.comboBox_COD_namper.addItem("72")
            self.comboBox_COD_namper.addItem("73")
            self.comboBox_COD_namper.addItem("74")
            self.comboBox_COD_namper.addItem("75")
            self.comboBox_COD_namper.addItem("76")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("78")
            self.comboBox_COD_namper.addItem("80")
            self.comboBox_COD_namper.addItem("81")
            self.comboBox_COD_namper.addItem("82")
            self.comboBox_COD_namper.addItem("83")
            self.comboBox_COD_namper.addItem("84")
            self.comboBox_COD_namper.addItem("85")
            self.comboBox_COD_namper.addItem("86")
            self.comboBox_COD_namper.addItem("87")
            self.comboBox_COD_namper.addItem("90")
            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("92")
            self.comboBox_COD_namper.addItem("93")
            self.comboBox_COD_namper.addItem("94")
            self.comboBox_COD_namper.addItem("95")
            self.comboBox_COD_namper.addItem("97")
            self.comboBox_COD_namper.addItem("98")

            self.countryNomper = 8

        case " Uruguay ":
            print(" Uruguay ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("91")
            self.comboBox_COD_namper.addItem("92")
            self.comboBox_COD_namper.addItem("93")
            self.comboBox_COD_namper.addItem("94")
            self.comboBox_COD_namper.addItem("95")
            self.comboBox_COD_namper.addItem("96")
            self.comboBox_COD_namper.addItem("97")
            self.comboBox_COD_namper.addItem("98")
            self.comboBox_COD_namper.addItem("99")

            self.countryNomper = 6

        case " Uzbekistan ":
            print(" Uzbekistan ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("3350")
            self.comboBox_COD_namper.addItem("5550")
            self.comboBox_COD_namper.addItem("5590")
            self.comboBox_COD_namper.addItem("6122")
            self.comboBox_COD_namper.addItem("6135")
            self.comboBox_COD_namper.addItem("6150")
            self.comboBox_COD_namper.addItem("6161")
            self.comboBox_COD_namper.addItem("6174")
            self.comboBox_COD_namper.addItem("6179")
            self.comboBox_COD_namper.addItem("6211")
            self.comboBox_COD_namper.addItem("6229")
            self.comboBox_COD_namper.addItem("6253")
            self.comboBox_COD_namper.addItem("6529")
            self.comboBox_COD_namper.addItem("6530")
            self.comboBox_COD_namper.addItem("6559")
            self.comboBox_COD_namper.addItem("6621")
            self.comboBox_COD_namper.addItem("6622")
            self.comboBox_COD_namper.addItem("6671")
            self.comboBox_COD_namper.addItem("6673")
            self.comboBox_COD_namper.addItem("6674")
            self.comboBox_COD_namper.addItem("6675")
            self.comboBox_COD_namper.addItem("6678")
            self.comboBox_COD_namper.addItem("6679")
            self.comboBox_COD_namper.addItem("6723")
            self.comboBox_COD_namper.addItem("6724")
            self.comboBox_COD_namper.addItem("6727")
            self.comboBox_COD_namper.addItem("6757")
            self.comboBox_COD_namper.addItem("6758")
            self.comboBox_COD_namper.addItem("6770")
            self.comboBox_COD_namper.addItem("6790")
            self.comboBox_COD_namper.addItem("6797")
            self.comboBox_COD_namper.addItem("6921")
            self.comboBox_COD_namper.addItem("6923")
            self.comboBox_COD_namper.addItem("6925")
            self.comboBox_COD_namper.addItem("6927")
            self.comboBox_COD_namper.addItem("6962")
            self.comboBox_COD_namper.addItem("6968")
            self.comboBox_COD_namper.addItem("7160")
            self.comboBox_COD_namper.addItem("7161")
            self.comboBox_COD_namper.addItem("7171")
            self.comboBox_COD_namper.addItem("7198")
            self.comboBox_COD_namper.addItem("7222")
            self.comboBox_COD_namper.addItem("7232")
            self.comboBox_COD_namper.addItem("7236")
            self.comboBox_COD_namper.addItem("7257")
            self.comboBox_COD_namper.addItem("7270")
            self.comboBox_COD_namper.addItem("7271")
            self.comboBox_COD_namper.addItem("7272")
            self.comboBox_COD_namper.addItem("7273")
            self.comboBox_COD_namper.addItem("7275")
            self.comboBox_COD_namper.addItem("7321")
            self.comboBox_COD_namper.addItem("7323")
            self.comboBox_COD_namper.addItem("7327")
            self.comboBox_COD_namper.addItem("7333")
            self.comboBox_COD_namper.addItem("7350")
            self.comboBox_COD_namper.addItem("7355")
            self.comboBox_COD_namper.addItem("7359")
            self.comboBox_COD_namper.addItem("7374")
            self.comboBox_COD_namper.addItem("7376")
            self.comboBox_COD_namper.addItem("7378")
            self.comboBox_COD_namper.addItem("7425")
            self.comboBox_COD_namper.addItem("7426")
            self.comboBox_COD_namper.addItem("7427")
            self.comboBox_COD_namper.addItem("7451")
            self.comboBox_COD_namper.addItem("7458")
            self.comboBox_COD_namper.addItem("7459")
            self.comboBox_COD_namper.addItem("7470")
            self.comboBox_COD_namper.addItem("7471")
            self.comboBox_COD_namper.addItem("7472")
            self.comboBox_COD_namper.addItem("7473")
            self.comboBox_COD_namper.addItem("7475")
            self.comboBox_COD_namper.addItem("7477")
            self.comboBox_COD_namper.addItem("7479")
            self.comboBox_COD_namper.addItem("7520")
            self.comboBox_COD_namper.addItem("7522")
            self.comboBox_COD_namper.addItem("7552")
            self.comboBox_COD_namper.addItem("7570")
            self.comboBox_COD_namper.addItem("7571")
            self.comboBox_COD_namper.addItem("7574")
            self.comboBox_COD_namper.addItem("7578")
            self.comboBox_COD_namper.addItem("7579")
            self.comboBox_COD_namper.addItem("7622")
            self.comboBox_COD_namper.addItem("7624")
            self.comboBox_COD_namper.addItem("7639")
            self.comboBox_COD_namper.addItem("7641")
            self.comboBox_COD_namper.addItem("7655")
            self.comboBox_COD_namper.addItem("7670")
            self.comboBox_COD_namper.addItem("7932")
            self.comboBox_COD_namper.addItem("7937")
            self.comboBox_COD_namper.addItem("7957")
            self.comboBox_COD_namper.addItem("7972")
            self.comboBox_COD_namper.addItem("7973")
            self.comboBox_COD_namper.addItem("7974")
            self.comboBox_COD_namper.addItem("7977")
            self.comboBox_COD_namper.addItem("7979")
            self.comboBox_COD_namper.addItem("8800")
            self.comboBox_COD_namper.addItem("9006")

            self.countryNomper = 5

        case " Venezuela, Bolivarian Republic of ":
            print(" Venezuela, Bolivarian Republic of ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("412")
            self.comboBox_COD_namper.addItem("414")
            self.comboBox_COD_namper.addItem("415")
            self.comboBox_COD_namper.addItem("416")
            self.comboBox_COD_namper.addItem("417")
            self.comboBox_COD_namper.addItem("418")
            self.comboBox_COD_namper.addItem("424")
            self.comboBox_COD_namper.addItem("426")

            self.countryNomper = 7

        case " Viet Nam ":
            print(" Viet Nam ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("3")
            self.comboBox_COD_namper.addItem("5")
            self.comboBox_COD_namper.addItem("7")
            self.comboBox_COD_namper.addItem("9")

            self.countryNomper = 8

        case " Zambia ":
            print(" Zambia ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("76")
            self.comboBox_COD_namper.addItem("77")
            self.comboBox_COD_namper.addItem("79")
            self.comboBox_COD_namper.addItem("95")
            self.comboBox_COD_namper.addItem("96")
            self.comboBox_COD_namper.addItem("97")
            self.comboBox_COD_namper.addItem("98")

            self.countryNomper = 6

        case " Zimbabwe ":
            print(" Zimbabwe ")
            self.comboBox_COD_namper.clear()

            self.comboBox_COD_namper.addItem("711")
            self.comboBox_COD_namper.addItem("731")
            self.comboBox_COD_namper.addItem("732")
            self.comboBox_COD_namper.addItem("733")
            self.comboBox_COD_namper.addItem("734")
            self.comboBox_COD_namper.addItem("735")
            self.comboBox_COD_namper.addItem("736")
            self.comboBox_COD_namper.addItem("737")
            self.comboBox_COD_namper.addItem("738")
            self.comboBox_COD_namper.addItem("739")
            self.comboBox_COD_namper.addItem("771")
            self.comboBox_COD_namper.addItem("781")

            self.countryNomper = 7
        case other:
            self.comboBox_COD_namper.clear()

            print("الرجاء ادخال الدوله")

    print("تم اختيار الدوله")
