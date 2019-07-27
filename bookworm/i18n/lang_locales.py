# coding: utf-8

"""This module lists major languages and their variances."""


locale_map = {
    "aa": ["DJ", "ER", "ET"],
    "af": ["NA", "ZA"],
    "ak": ["GH"],
    "am": ["ET"],
    "ar": [
        "SA",
        "AE",
        "BH",
        "DJ",
        "DZ",
        "EG",
        "ER",
        "IL",
        "IQ",
        "JO",
        "KM",
        "KW",
        "LB",
        "LY",
        "MA",
        "MR",
        "OM",
        "PS",
        "QA",
        "SD",
        "SO",
        "SS",
        "SY",
        "TD",
        "TN",
        "YE",
    ],
    "as": ["IN"],
    "ba": ["RU"],
    "be": ["BY"],
    "bg": ["BG"],
    "bn": ["BD", "IN"],
    "bo": ["CN", "IN"],
    "br": ["FR"],
    "ca": ["AD", "ES", "ES", "FR", "IT"],
    "ce": ["RU"],
    "co": ["FR"],
    "cs": ["CZ"],
    "cu": ["RU"],
    "cy": ["GB"],
    "da": ["DK", "GL"],
    "de": ["AT", "BE", "CH", "DE", "IT", "LI", "LU"],
    "dv": ["MV"],
    "dz": ["BT"],
    "ee": ["GH", "TG"],
    "el": ["CY", "GR"],
    "en": [
        "US",
        "GB",
        "AG",
        "AI",
        "AS",
        "AT",
        "AU",
        "BB",
        "BE",
        "BI",
        "BM",
        "BS",
        "BW",
        "BZ",
        "CA",
        "CC",
        "CH",
        "CK",
        "CM",
        "CX",
        "CY",
        "DE",
        "DK",
        "DM",
        "ER",
        "FI",
        "FJ",
        "FK",
        "FM",
        "GD",
        "GG",
        "GH",
        "GI",
        "GM",
        "GU",
        "GY",
        "HK",
        "ID",
        "IE",
        "IL",
        "IM",
        "IN",
        "IO",
        "JE",
        "JM",
        "KE",
        "KI",
        "KN",
        "KY",
        "LC",
        "LR",
        "LS",
        "MG",
        "MH",
        "MO",
        "MP",
        "MS",
        "MT",
        "MU",
        "MW",
        "MY",
        "NA",
        "NF",
        "NG",
        "NL",
        "NR",
        "NU",
        "NZ",
        "PG",
        "PH",
        "PK",
        "PN",
        "PR",
        "PW",
        "RW",
        "SB",
        "SC",
        "SD",
        "SE",
        "SG",
        "SH",
        "SI",
        "SL",
        "SS",
        "SX",
        "SZ",
        "TC",
        "TK",
        "TO",
        "TT",
        "TV",
        "TZ",
        "UG",
        "UM",
        "VC",
        "VG",
        "VI",
        "VU",
        "WS",
        "ZA",
        "ZM",
        "ZW",
    ],
    "es": [
        "ES",
        "US",
        "AR",
        "BO",
        "BR",
        "CL",
        "CO",
        "CR",
        "CU",
        "DO",
        "EC",
        "GQ",
        "GT",
        "HN",
        "MX",
        "NI",
        "PA",
        "PE",
        "PH",
        "PR",
        "PY",
        "SV",
        "UY",
        "VE",
    ],
    "et": ["EE"],
    "eu": ["ES"],
    "fa": ["IR"],
    "ff": ["CM", "GN", "MR", "NG"],
    "fi": ["FI"],
    "fo": ["DK", "FO"],
    "fr": [
        "BE",
        "BF",
        "BI",
        "BJ",
        "BL",
        "CA",
        "CD",
        "CF",
        "CG",
        "CH",
        "CI",
        "CM",
        "DJ",
        "DZ",
        "FR",
        "GA",
        "GF",
        "GN",
        "GP",
        "GQ",
        "HT",
        "KM",
        "LU",
        "MA",
        "MC",
        "MF",
        "MG",
        "ML",
        "MQ",
        "MR",
        "MU",
        "NC",
        "NE",
        "PF",
        "PM",
        "RE",
        "RW",
        "SC",
        "SN",
        "SY",
        "TD",
        "TG",
        "TN",
        "VU",
        "WF",
        "YT",
    ],
    "fy": ["NL"],
    "ga": ["IE"],
    "gd": ["GB"],
    "gl": ["ES"],
    "gn": ["PY"],
    "gu": ["IN"],
    "gv": ["IM"],
    "he": ["IL"],
    "hi": ["IN"],
    "hr": ["BA", "HR"],
    "hu": ["HU"],
    "hy": ["AM"],
    "ia": ["FR"],
    "id": ["ID"],
    "ig": ["NG"],
    "ii": ["CN"],
    "is": ["IS"],
    "it": ["CH", "IT", "SM"],
    "ja": ["JP"],
    "ka": ["GE"],
    "ki": ["KE"],
    "kk": ["KZ"],
    "kl": ["GL"],
    "km": ["KH"],
    "kn": ["IN"],
    "ko": ["KP", "KR"],
    "kr": ["NG"],
    "kw": ["GB"],
    "ky": ["KG"],
    "lb": ["LU"],
    "lg": ["UG"],
    "ln": ["AO", "CD", "CF", "CG"],
    "lo": ["LA"],
    "lt": ["LT"],
    "lu": ["CD"],
    "lv": ["LV"],
    "mg": ["MG"],
    "mi": ["NZ"],
    "mk": ["MK"],
    "ml": ["IN"],
    "mn": ["MN"],
    "mr": ["IN"],
    "ms": ["BN", "MY", "SG"],
    "mt": ["MT"],
    "my": ["MM"],
    "nb": ["NO", "SJ"],
    "nd": ["ZW"],
    "ne": ["IN", "NP"],
    "nl": ["AW", "BE", "BQ", "CW", "NL", "SR", "SX"],
    "nn": ["NO"],
    "nr": ["ZA"],
    "oc": ["FR"],
    "om": ["ET", "KE"],
    "or": ["IN"],
    "os": ["GE", "RU"],
    "pa": ["IN"],
    "pl": ["PL"],
    "ps": ["AF"],
    "pt": ["AO", "BR", "CH", "CV", "GQ", "GW", "LU", "MO", "MZ", "PT", "ST", "TL"],
    "rm": ["CH"],
    "rn": ["BI"],
    "ro": ["MD", "RO"],
    "ru": ["BY", "KG", "KZ", "MD", "RU", "UA"],
    "rw": ["RW"],
    "sa": ["IN"],
    "se": ["FI", "NO", "SE"],
    "sg": ["CF"],
    "si": ["LK"],
    "sk": ["SK"],
    "sl": ["SI"],
    "so": ["DJ", "ET", "KE", "SO"],
    "sq": ["AL", "MK", "XK"],
    "ss": ["SZ", "ZA"],
    "st": ["LS", "ZA"],
    "sv": ["AX", "FI", "SE"],
    "sw": ["CD", "KE", "TZ", "UG"],
    "ta": ["IN", "LK", "MY", "SG"],
    "te": ["IN"],
    "th": ["TH"],
    "ti": ["ER", "ET"],
    "tk": ["TM"],
    "tn": ["BW", "ZA"],
    "to": ["TO"],
    "tr": ["CY", "TR"],
    "ts": ["ZA"],
    "tt": ["RU"],
    "ug": ["CN"],
    "uk": ["UA"],
    "ur": ["IN", "PK"],
    "ve": ["ZA"],
    "vi": ["VN"],
    "wo": ["SN"],
    "xh": ["ZA"],
    "yo": ["BJ", "NG"],
    "zh": ["CN", "HK", "MO", "SG", "TW"],
    "zu": ["ZA"],
}