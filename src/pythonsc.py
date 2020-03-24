from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active

import json

y = [
  {
    "code": "madhya pradesh",
    "name": "MADHYA PRADESH",
    "value": 4,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "0755-2527177",
    "lockDownStatus": "",
    "latitude": "22.9734",
    "longitude": "78.6569",
    "testCentres": [],
    "markerInfo": [],
    "_i": 0
  },
  {
    "code": "uttar pradesh",
    "name": "UTTAR PRADESH",
    "value": 29,
    "deaths": "0",
    "recoveries": "9",
    "helpline": "18001805145",
    "lockDownStatus": "",
    "latitude": "26.8467",
    "longitude": "80.9462",
    "testCentres": [],
    "markerInfo": [],
    "_i": 1
  },
  {
    "code": "karnataka",
    "name": "KARNATAKA",
    "value": 26,
    "deaths": "1",
    "recoveries": "2",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "15.3173",
    "longitude": "75.7139",
    "testCentres": [],
    "markerInfo": [],
    "_i": 2
  },
  {
    "code": "nagaland",
    "name": "NAGALAND",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "7005539653",
    "lockDownStatus": "",
    "latitude": "26.1584",
    "longitude": "94.5624",
    "testCentres": [],
    "markerInfo": [],
    "_i": 3
  },
  {
    "code": "bihar",
    "name": "BIHAR",
    "value": 2,
    "deaths": "1",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "25.0961",
    "longitude": "85.3131",
    "testCentres": [],
    "markerInfo": [],
    "_i": 4
  },
  {
    "code": "lakshadweep",
    "name": "LAKSHADWEEP",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "4896263742",
    "lockDownStatus": "",
    "latitude": "10.5667",
    "longitude": "72.6417",
    "testCentres": [],
    "markerInfo": [],
    "_i": 5
  },
  {
    "code": "andaman and nicobar",
    "name": "ANDAMAN AND NICOBAR",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "03192-232102",
    "lockDownStatus": "",
    "latitude": "11.7401",
    "longitude": "92.6586",
    "testCentres": [],
    "markerInfo": [],
    "_i": 6
  },
  {
    "code": "assam",
    "name": "ASSAM",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "6913347770",
    "lockDownStatus": "",
    "latitude": "26.2006",
    "longitude": "92.9376",
    "testCentres": [],
    "markerInfo": [],
    "_i": 7
  },
  {
    "code": "west bengal",
    "name": "WEST BENGAL",
    "value": 7,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "3323412600",
    "lockDownStatus": "",
    "latitude": "22.9868",
    "longitude": "87.855",
    "testCentres": [],
    "markerInfo": [],
    "_i": 8
  },
  {
    "code": "puducherry",
    "name": "PUDUCHERRY",
    "value": 1,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "11.9416",
    "longitude": "79.8083",
    "testCentres": [],
    "markerInfo": [],
    "_i": 9
  },
  {
    "code": "daman and diu",
    "name": "DAMAN AND DIU",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "20.4283",
    "longitude": "72.8397",
    "testCentres": [],
    "markerInfo": [],
    "_i": 10
  },
  {
    "code": "gujarat",
    "name": "GUJARAT",
    "value": 18,
    "deaths": "1",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "22.2587",
    "longitude": "71.1924",
    "testCentres": [
      {
        "name": "Unipath Specialty laboratory limited, 102, Sanoma Plaza, Opposite Parimal Garden, Besides JMC House, Ellisbridge, Ahmedabad",
        "gov": False
      },
      {
        "name": "Supratech Micropath Laboratory & Research Institute Pvt Ltd, Kedar, Ahmedabad",
        "gov": False
      }
    ],
    "markerInfo": [
      {
        "address_components": [
          {
            "long_name": "Ahmedabad",
            "short_name": "Ahmedabad",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Tulsibag Society",
            "short_name": "Tulsibag Society",
            "types": [
              "neighborhood",
              "political"
            ]
          },
          {
            "long_name": "Ambawadi",
            "short_name": "Ambawadi",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Ahmedabad",
            "short_name": "Ahmedabad",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Gujarat",
            "short_name": "GJ",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "380006",
            "short_name": "380006",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "102, 1st Floor, Sanoma Plaza, Sheth Mangald Road, Opp. Parimal Garden, Ellisbridge, Tulsibag Society, Ambawadi, Ahmedabad, Gujarat 380006, India",
        "geometry": {
          "location": {
            "lat": 23.0191034,
            "lng": 72.5556622
          },
          "location_type": "GEOMETRIC_CENTER",
          "viewport": {
            "northeast": {
              "lat": 23.0204523802915,
              "lng": 72.5570111802915
            },
            "southwest": {
              "lat": 23.0177544197085,
              "lng": 72.55431321970849
            }
          }
        },
        "place_id": "ChIJ218wSuOEXjkRl21tdEK3GuI",
        "plus_code": {
          "compound_code": "2H94+J7 Ahmedabad, Gujarat, India",
          "global_code": "7JMJ2H94+J7"
        },
        "types": [
          "establishment",
          "point_of_interest"
        ]
      },
      {
        "address_components": [
          {
            "long_name": "Ahmedabad",
            "short_name": "Ahmedabad",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Ellisbridge",
            "short_name": "Ellisbridge",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Ahmedabad",
            "short_name": "Ahmedabad",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Gujarat",
            "short_name": "GJ",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "380006",
            "short_name": "380006",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "Neuberg Supratech, Ground Floor, Kedar Builiding, Opp. Krupa petrol Pump Parimal garden, Ellisbridge, Ahmedabad, Gujarat 380006, India",
        "geometry": {
          "location": {
            "lat": 23.0198295,
            "lng": 72.5592869
          },
          "location_type": "GEOMETRIC_CENTER",
          "viewport": {
            "northeast": {
              "lat": 23.0211784802915,
              "lng": 72.56063588029151
            },
            "southwest": {
              "lat": 23.0184805197085,
              "lng": 72.55793791970851
            }
          }
        },
        "place_id": "ChIJcRjrqfyEXjkREHaTL0JZ5GI",
        "plus_code": {
          "compound_code": "2H95+WP Ahmedabad, Gujarat, India",
          "global_code": "7JMJ2H95+WP"
        },
        "types": [
          "establishment",
          "health",
          "point_of_interest"
        ]
      }
    ],
    "_i": 11
  },
  {
    "code": "rajasthan",
    "name": "RAJASTHAN",
    "value": 27,
    "deaths": "0",
    "recoveries": "3",
    "helpline": "0141-2225624",
    "lockDownStatus": "",
    "latitude": "27.0238",
    "longitude": "74.2179",
    "testCentres": [],
    "markerInfo": [],
    "_i": 12
  },
  {
    "code": "dadra and nagar havelli",
    "name": "DADRA AND NAGAR HAVELLI",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "20.1809",
    "longitude": "73.0169",
    "testCentres": [],
    "markerInfo": [],
    "_i": 13
  },
  {
    "code": "chhattisgarh",
    "name": "CHHATTISGARH",
    "value": 1,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "077122-35091",
    "lockDownStatus": "",
    "latitude": "21.2787",
    "longitude": "81.8661",
    "testCentres": [],
    "markerInfo": [],
    "_i": 14
  },
  {
    "code": "tamil nadu",
    "name": "TAMIL NADU",
    "value": 9,
    "deaths": "0",
    "recoveries": "1",
    "helpline": "044-29510500",
    "lockDownStatus": "",
    "latitude": "11.1271",
    "longitude": "78.6569",
    "testCentres": [
      {
        "name": "Dept. of Clinical Virology, CMC, Vellore",
        "gov": False
      },
      {
        "name": "Department of Laboratory Services, Apollo Hospitals Enterprise Ltd, Chennai",
        "gov": False
      }
    ],
    "markerInfo": [
      {
        "address_components": [
          {
            "long_name": "IDA Scudder Road",
            "short_name": "IDA Scudder Rd",
            "types": [
              "route"
            ]
          },
          {
            "long_name": "Vellore",
            "short_name": "Vellore",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Vellore",
            "short_name": "Vellore",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Tamil Nadu",
            "short_name": "TN",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "632004",
            "short_name": "632004",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "IDA Scudder Rd, Vellore, Tamil Nadu 632004, India",
        "geometry": {
          "location": {
            "lat": 12.9246021,
            "lng": 79.1348129
          },
          "location_type": "GEOMETRIC_CENTER",
          "viewport": {
            "northeast": {
              "lat": 12.9259510802915,
              "lng": 79.13616188029151
            },
            "southwest": {
              "lat": 12.9232531197085,
              "lng": 79.13346391970849
            }
          }
        },
        "place_id": "ChIJ_9xuxpQ4rTsRLcfZs2w55Hk",
        "plus_code": {
          "compound_code": "W4FM+RW Vellore, Tamil Nadu, India",
          "global_code": "7J4XW4FM+RW"
        },
        "types": [
          "establishment",
          "health",
          "point_of_interest",
          "university"
        ]
      },
      {
        "address_components": [
          {
            "long_name": "Chennai",
            "short_name": "Chennai",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Thousand Lights West",
            "short_name": "Thousand Lights West",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_2"
            ]
          },
          {
            "long_name": "Thousand Lights",
            "short_name": "Thousand Lights",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Chennai",
            "short_name": "Chennai",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Tamil Nadu",
            "short_name": "TN",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "600006",
            "short_name": "600006",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "'Sunny Side', East Block, 3rd Floor, 8/17, Shafee Mohamed Road, Thousand Lights West, Thousand Lights, Chennai, Tamil Nadu 600006, India",
        "geometry": {
          "location": {
            "lat": 13.0610854,
            "lng": 80.2533572
          },
          "location_type": "GEOMETRIC_CENTER",
          "viewport": {
            "northeast": {
              "lat": 13.0624343802915,
              "lng": 80.2547061802915
            },
            "southwest": {
              "lat": 13.0597364197085,
              "lng": 80.25200821970849
            }
          }
        },
        "place_id": "ChIJlXhx3GpmUjoRbXW2UZSybCY",
        "plus_code": {
          "compound_code": "3763+C8 Chennai, Tamil Nadu, India",
          "global_code": "7M523763+C8"
        },
        "types": [
          "establishment",
          "point_of_interest"
        ]
      }
    ],
    "_i": 15
  },
  {
    "code": "chandigarh",
    "name": "CHANDIGARH",
    "value": 5,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "9779558282",
    "lockDownStatus": "",
    "latitude": "30.7333",
    "longitude": "76.7794",
    "testCentres": [],
    "markerInfo": [],
    "_i": 16
  },
  {
    "code": "punjab",
    "name": "PUNJAB",
    "value": 21,
    "deaths": "1",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "31.1471",
    "longitude": "75.3412",
    "testCentres": [],
    "markerInfo": [],
    "_i": 17
  },
  {
    "code": "haryana",
    "name": "HARYANA",
    "value": 21,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "8558893911",
    "lockDownStatus": "",
    "latitude": "29.0588",
    "longitude": "76.0856",
    "testCentres": [
      {
        "name": "Strand Life Sciences, A-17, Sector 34, Gurugram",
        "gov": False
      },
      {
        "name": "SRL Limited, GP26, Sector 18, Gurugram",
        "gov": False
      }
    ],
    "markerInfo": [
      {
        "address_components": [
          {
            "long_name": "A-17",
            "short_name": "A-17",
            "types": [
              "premise"
            ]
          },
          {
            "long_name": "Info Technology Park",
            "short_name": "Info Technology Park",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_2"
            ]
          },
          {
            "long_name": "Sector 34",
            "short_name": "Sector 34",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Gurugram",
            "short_name": "Gurugram",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Gurgaon",
            "short_name": "Gurgaon",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Haryana",
            "short_name": "HR",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "122001",
            "short_name": "122001",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "A-17, Info Technology Park, Sector 34, Gurugram, Haryana 122001, India",
        "geometry": {
          "location": {
            "lat": 28.4294379,
            "lng": 77.01553849999999
          },
          "location_type": "ROOFTOP",
          "viewport": {
            "northeast": {
              "lat": 28.4307868802915,
              "lng": 77.0168874802915
            },
            "southwest": {
              "lat": 28.4280889197085,
              "lng": 77.0141895197085
            }
          }
        },
        "place_id": "ChIJ-xzpLKgZDTkR9llFl00naSw",
        "plus_code": {
          "compound_code": "C2H8+Q6 Gurugram, Haryana, India",
          "global_code": "7JWVC2H8+Q6"
        },
        "types": [
          "establishment",
          "health",
          "point_of_interest"
        ]
      },
      {
        "address_components": [
          {
            "long_name": "Udyog Vihar",
            "short_name": "Udyog Vihar",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_2"
            ]
          },
          {
            "long_name": "Sector 18",
            "short_name": "Sector 18",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Gurugram",
            "short_name": "Gurugram",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Gurgaon",
            "short_name": "Gurgaon",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Haryana",
            "short_name": "HR",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "122015",
            "short_name": "122015",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "SRL,REFERENCE LAB, GP-26, MARUTI INDUSTRIAL ESTATE, Udyog Vihar, Sector 18, Gurugram, Haryana 122015, India",
        "geometry": {
          "location": {
            "lat": 28.489104,
            "lng": 77.061689
          },
          "location_type": "GEOMETRIC_CENTER",
          "viewport": {
            "northeast": {
              "lat": 28.4904529802915,
              "lng": 77.06303798029151
            },
            "southwest": {
              "lat": 28.48775501970849,
              "lng": 77.06034001970849
            }
          }
        },
        "place_id": "ChIJZZqW8gsZDTkR19n9XCS5pNQ",
        "plus_code": {
          "compound_code": "F3Q6+JM Sector 18, Gurugram, Haryana, India",
          "global_code": "7JWVF3Q6+JM"
        },
        "types": [
          "establishment",
          "health",
          "point_of_interest"
        ]
      }
    ],
    "_i": 18
  },
  {
    "code": "andhra pradesh",
    "name": "ANDHRA PRADESH",
    "value": 5,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "0866-2410978",
    "lockDownStatus": "Partial",
    "latitude": "15.9129",
    "longitude": "79.74",
    "testCentres": [],
    "markerInfo": [],
    "_i": 19
  },
  {
    "code": "maharashtra",
    "name": "MAHARASHTRA",
    "value": 67,
    "deaths": "2",
    "recoveries": "0",
    "helpline": "020-26127394",
    "lockDownStatus": "Full lockdown",
    "latitude": "19.7515",
    "longitude": "75.7139",
    "testCentres": [
      {
        "name": "Thyrocare Technologies Limited, D37/1, TTC MIDC, Turbhe, Navi Mumbai",
        "gov": False
      },
      {
        "name": "Suburban Diagnostics (India) Pvt. Ltd., 306, 307/T, 3rd Floor, Sunshine Bld., Andheri (W), Mumbai",
        "gov": False
      },
      {
        "name": "Metropolis Healthcare Ltd, Unit No. 409-416, 4th Floor, Commercial Building-1, Kohinoor Mall, Mumbai",
        "gov": False
      },
      {
        "name": "Sir H.N. Reliance Foundation Hospital and Research Centre, Molecular Medicine, Reliance Life Sciences Pvt. Ltd., R-282, TTC Industrial Area, Rabale, Navi Mumbai",
        "gov": False
      },
      {
        "name": "SRL Limited, Prime Square Building, Plot No 1, Gaiwadi Industrial Estate, SV Road, Goregaon, Mumbai",
        "gov": False
      }
    ],
    "markerInfo": [
      {
        "address_components": [
          {
            "long_name": "1",
            "short_name": "1",
            "types": [
              "street_number"
            ]
          },
          {
            "long_name": "Turbhe Road",
            "short_name": "Turbhe Rd",
            "types": [
              "route"
            ]
          },
          {
            "long_name": "Juhu Nagar",
            "short_name": "Juhu Nagar",
            "types": [
              "neighborhood",
              "political"
            ]
          },
          {
            "long_name": "T.T.C. Industrial Area",
            "short_name": "T.T.C. Industrial Area",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_3"
            ]
          },
          {
            "long_name": "MIDC Industrial Area",
            "short_name": "MIDC Industrial Area",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_2"
            ]
          },
          {
            "long_name": "Pawne",
            "short_name": "Pawne",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Navi Mumbai",
            "short_name": "Navi Mumbai",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Thane",
            "short_name": "Thane",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Maharashtra",
            "short_name": "MH",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "400703",
            "short_name": "400703",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "1, Turbhe Rd, Juhu Nagar, T.T.C. Industrial Area, MIDC Industrial Area, Pawne, Navi Mumbai, Maharashtra 400703, India",
        "geometry": {
          "location": {
            "lat": 19.0742538,
            "lng": 72.9997525
          },
          "location_type": "ROOFTOP",
          "viewport": {
            "northeast": {
              "lat": 19.0756027802915,
              "lng": 73.00110148029151
            },
            "southwest": {
              "lat": 19.07290481970849,
              "lng": 72.9984035197085
            }
          }
        },
        "place_id": "ChIJD3inBTbB5zsRnHHnwFICTaQ",
        "plus_code": {
          "compound_code": "3XFX+PW Navi Mumbai, Maharashtra, India",
          "global_code": "7JFJ3XFX+PW"
        },
        "types": [
          "establishment",
          "point_of_interest"
        ]
      },
      {
        "address_components": [
          {
            "long_name": "Mercedes Showroom",
            "short_name": "Mercedes Showroom",
            "types": []
          },
          {
            "long_name": "Sundervan Complex",
            "short_name": "Sundervan Complex",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_3"
            ]
          },
          {
            "long_name": "Shastri Nagar",
            "short_name": "Shastri Nagar",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_2"
            ]
          },
          {
            "long_name": "Andheri West",
            "short_name": "Andheri West",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Mumbai",
            "short_name": "Mumbai",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Mumbai Suburban",
            "short_name": "Mumbai Suburban",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Maharashtra",
            "short_name": "MH",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "400053",
            "short_name": "400053",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "Aston, 2nd floor, Sundervan Complex , Opp. Union Bank, above Mercedes Showroom, Sundervan Complex, Shastri Nagar, Andheri West, Mumbai, Maharashtra 400053, India",
        "geometry": {
          "location": {
            "lat": 19.137332,
            "lng": 72.8260739
          },
          "location_type": "GEOMETRIC_CENTER",
          "viewport": {
            "northeast": {
              "lat": 19.1386809802915,
              "lng": 72.82742288029151
            },
            "southwest": {
              "lat": 19.1359830197085,
              "lng": 72.82472491970849
            }
          }
        },
        "partial_match": True,
        "place_id": "ChIJ-SswqIe35zsRbU6gMdkvsLw",
        "plus_code": {
          "compound_code": "4RPG+WC Andheri West, Mumbai, Maharashtra, India",
          "global_code": "7JFJ4RPG+WC"
        },
        "types": [
          "establishment",
          "health",
          "point_of_interest"
        ]
      },
      {
        "address_components": [
          {
            "long_name": "Mumbai",
            "short_name": "Mumbai",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Premier Residencies",
            "short_name": "Premier Residencies",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_2"
            ]
          },
          {
            "long_name": "Kurla",
            "short_name": "Kurla",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Mumbai Suburban",
            "short_name": "Mumbai Suburban",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Maharashtra",
            "short_name": "MH",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "400070",
            "short_name": "400070",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "4th Floor, Commerical Building 1-A, Kohinoor City Mall, Off LBS Marg, Vidyavihar (West), Premier Residencies, Kurla, Mumbai, Maharashtra 400070, India",
        "geometry": {
          "location": {
            "lat": 19.0820107,
            "lng": 72.88572049999999
          },
          "location_type": "GEOMETRIC_CENTER",
          "viewport": {
            "northeast": {
              "lat": 19.0833596802915,
              "lng": 72.8870694802915
            },
            "southwest": {
              "lat": 19.0806617197085,
              "lng": 72.8843715197085
            }
          }
        },
        "place_id": "ChIJAZ7RBYTI5zsRDiEJG__Wnrg",
        "plus_code": {
          "compound_code": "3VJP+R7 Mumbai, Maharashtra, India",
          "global_code": "7JFJ3VJP+R7"
        },
        "types": [
          "doctor",
          "establishment",
          "health",
          "point_of_interest"
        ]
      },
      {
        "address_components": [
          {
            "long_name": "R-282",
            "short_name": "R-282",
            "types": [
              "street_number"
            ]
          },
          {
            "long_name": "Thane - Belapur Road",
            "short_name": "Thane - Belapur Rd",
            "types": [
              "route"
            ]
          },
          {
            "long_name": "T.T.C. Industrial Area",
            "short_name": "T.T.C. Industrial Area",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_3"
            ]
          },
          {
            "long_name": "MIDC Industrial Area",
            "short_name": "MIDC Industrial Area",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_2"
            ]
          },
          {
            "long_name": "Rabale",
            "short_name": "Rabale",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Navi Mumbai",
            "short_name": "Navi Mumbai",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Thane",
            "short_name": "Thane",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Maharashtra",
            "short_name": "MH",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "400701",
            "short_name": "400701",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "of MIDC, R-282, Thane - Belapur Rd, T.T.C. Industrial Area, MIDC Industrial Area, Rabale, Navi Mumbai, Maharashtra 400701, India",
        "geometry": {
          "location": {
            "lat": 19.139211,
            "lng": 73.00445719999999
          },
          "location_type": "ROOFTOP",
          "viewport": {
            "northeast": {
              "lat": 19.1405599802915,
              "lng": 73.00580618029149
            },
            "southwest": {
              "lat": 19.1378620197085,
              "lng": 73.00310821970848
            }
          }
        },
        "place_id": "ChIJF-0LNKjA5zsRdXfTNKYbBZ8",
        "plus_code": {
          "compound_code": "42Q3+MQ Navi Mumbai, Maharashtra, India",
          "global_code": "7JFM42Q3+MQ"
        },
        "types": [
          "establishment",
          "point_of_interest"
        ]
      },
      {
        "address_components": [
          {
            "long_name": "Mumbai",
            "short_name": "Mumbai",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Piramal Nagar",
            "short_name": "Piramal Nagar",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_2"
            ]
          },
          {
            "long_name": "Goregaon West",
            "short_name": "Goregaon West",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Mumbai Suburban",
            "short_name": "Mumbai Suburban",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Maharashtra",
            "short_name": "MH",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "400062",
            "short_name": "400062",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "Plot No 1, Prime Square building, Gaiwadi Industrial, estate, Next to Patel Petrol Pump, Opposite Mahesh Nagar, S.V. Road,, Goregaon West, Piramal Nagar, Goregaon West, Mumbai, Maharashtra 400062, India",
        "geometry": {
          "location": {
            "lat": 19.1713976,
            "lng": 72.845615
          },
          "location_type": "GEOMETRIC_CENTER",
          "viewport": {
            "northeast": {
              "lat": 19.1727465802915,
              "lng": 72.8469639802915
            },
            "southwest": {
              "lat": 19.1700486197085,
              "lng": 72.8442660197085
            }
          }
        },
        "place_id": "ChIJmzdad1a25zsRG-KyiP5LmIU",
        "plus_code": {
          "compound_code": "5RCW+H6 Mumbai, Maharashtra, India",
          "global_code": "7JFJ5RCW+H6"
        },
        "types": [
          "establishment",
          "health",
          "point_of_interest"
        ]
      }
    ],
    "_i": 20
  },
  {
    "code": "himachal pradesh",
    "name": "HIMACHAL PRADESH",
    "value": 2,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "31.1048",
    "longitude": "77.1734",
    "testCentres": [],
    "markerInfo": [],
    "_i": 21
  },
  {
    "code": "meghalaya",
    "name": "MEGHALAYA",
    "value": 95,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "9366090748",
    "lockDownStatus": "",
    "latitude": "25.467",
    "longitude": "91.3662",
    "testCentres": [],
    "markerInfo": [],
    "_i": 22
  },
  {
    "code": "kerala",
    "name": "KERALA",
    "value": 67,
    "deaths": "0",
    "recoveries": "3",
    "helpline": "0471-2552056",
    "lockDownStatus": "",
    "latitude": "10.8505",
    "longitude": "76.2711",
    "testCentres": [],
    "markerInfo": [],
    "_i": 23
  },
  {
    "code": "telangana",
    "name": "TELANGANA",
    "value": 26,
    "deaths": "0",
    "recoveries": "1",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "18.1124",
    "longitude": "79.0193",
    "testCentres": [
      {
        "name": "Laboratory Services, Apollo Hospitals, 6th Floor, Health Street\nBuilding, Jubilee Hills, Hyderabad",
        "gov": False
      }
    ],
    "markerInfo": [
      {
        "address_components": [
          {
            "long_name": "Bharatiya Vidya Bhavan School",
            "short_name": "Bharatiya Vidya Bhavan School",
            "types": []
          },
          {
            "long_name": "Road Number 72",
            "short_name": "Rd Number 72",
            "types": [
              "route"
            ]
          },
          {
            "long_name": "Jubilee Hills",
            "short_name": "Jubilee Hills",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "Hyderabad",
            "short_name": "Hyderabad",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "Hyderabad",
            "short_name": "Hyderabad",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Telangana",
            "short_name": "Telangana",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "500033",
            "short_name": "500033",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "Rd Number 72, opp. Bharatiya Vidya Bhavan School, Jubilee Hills, Hyderabad, Telangana 500033, India",
        "geometry": {
          "location": {
            "lat": 17.4148701,
            "lng": 78.4123403
          },
          "location_type": "GEOMETRIC_CENTER",
          "viewport": {
            "northeast": {
              "lat": 17.4162190802915,
              "lng": 78.41368928029149
            },
            "southwest": {
              "lat": 17.41352111970849,
              "lng": 78.41099131970849
            }
          }
        },
        "place_id": "ChIJk_Mt28iWyzsRYN_G4yswLfs",
        "plus_code": {
          "compound_code": "CC76+WW Jubilee Hills, Hyderabad, Telangana, India",
          "global_code": "7J9WCC76+WW"
        },
        "types": [
          "establishment",
          "health",
          "hospital",
          "point_of_interest"
        ]
      }
    ],
    "_i": 24
  },
  {
    "code": "mizoram",
    "name": "MIZORAM",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "102",
    "lockDownStatus": "",
    "latitude": "23.1645",
    "longitude": "92.9376",
    "testCentres": [],
    "markerInfo": [],
    "_i": 25
  },
  {
    "code": "tripura",
    "name": "TRIPURA",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "0381-2315879",
    "lockDownStatus": "",
    "latitude": "23.9408",
    "longitude": "91.9882",
    "testCentres": [],
    "markerInfo": [],
    "_i": 26
  },
  {
    "code": "manipur",
    "name": "MANIPUR",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "3852411668",
    "lockDownStatus": "",
    "latitude": "24.6637",
    "longitude": "93.9063",
    "testCentres": [],
    "markerInfo": [],
    "_i": 27
  },
  {
    "code": "arunanchal pradesh",
    "name": "ARUNANCHAL PRADESH",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "9536055743",
    "lockDownStatus": "",
    "latitude": "15.9129",
    "longitude": "79.74",
    "testCentres": [],
    "markerInfo": [],
    "_i": 28
  },
  {
    "code": "jharkand",
    "name": "JHARKAND",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "23.6102",
    "longitude": "85.2799",
    "testCentres": [],
    "markerInfo": [],
    "_i": 29
  },
  {
    "code": "goa",
    "name": "GOA",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "15.2993",
    "longitude": "74.124",
    "testCentres": [],
    "markerInfo": [],
    "_i": 30
  },
  {
    "code": "nct of delhi",
    "name": "NCT OF DELHI",
    "value": 29,
    "deaths": "1",
    "recoveries": "5",
    "helpline": "011-22307145",
    "lockDownStatus": "",
    "latitude": "28.7041",
    "longitude": "77.1025",
    "testCentres": [
      {
        "name": "Lal Path Labs, Block -E, Sector 18, Rohini, Delhi",
        "gov": False
      }
    ],
    "markerInfo": [
      {
        "address_components": [
          {
            "long_name": "National Reference laboratory",
            "short_name": "National Reference laboratory",
            "types": [
              "establishment",
              "point_of_interest"
            ]
          },
          {
            "long_name": "B7 Road",
            "short_name": "B7 Rd",
            "types": [
              "route"
            ]
          },
          {
            "long_name": "Block E",
            "short_name": "Block E",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_3"
            ]
          },
          {
            "long_name": "Sector 18",
            "short_name": "Sector 18",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_2"
            ]
          },
          {
            "long_name": "Rohini",
            "short_name": "Rohini",
            "types": [
              "political",
              "sublocality",
              "sublocality_level_1"
            ]
          },
          {
            "long_name": "New Delhi",
            "short_name": "New Delhi",
            "types": [
              "locality",
              "political"
            ]
          },
          {
            "long_name": "North West Delhi",
            "short_name": "North West Delhi",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Delhi",
            "short_name": "DL",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "India",
            "short_name": "IN",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "110085",
            "short_name": "110085",
            "types": [
              "postal_code"
            ]
          }
        ],
        "formatted_address": "National Reference laboratory, B7 Rd, Block E, Sector 18, Rohini, New Delhi, Delhi 110085, India",
        "geometry": {
          "location": {
            "lat": 28.7388534,
            "lng": 77.1364103
          },
          "location_type": "GEOMETRIC_CENTER",
          "viewport": {
            "northeast": {
              "lat": 28.7402023802915,
              "lng": 77.1377592802915
            },
            "southwest": {
              "lat": 28.7375044197085,
              "lng": 77.13506131970848
            }
          }
        },
        "place_id": "ChIJcd7KIw4BDTkRTu95sLLREoE",
        "plus_code": {
          "compound_code": "P4QP+GH Rohini, New Delhi, Delhi, India",
          "global_code": "7JWVP4QP+GH"
        },
        "types": [
          "establishment",
          "health",
          "point_of_interest"
        ]
      }
    ],
    "_i": 31
  },
  {
    "code": "odisha",
    "name": "ODISHA",
    "value": 2,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "9439994859",
    "lockDownStatus": "",
    "latitude": "20.9517",
    "longitude": "85.0985",
    "testCentres": [],
    "markerInfo": [],
    "_i": 32
  },
  {
    "code": "jammu and kashmir",
    "name": "JAMMU AND KASHMIR",
    "value": 17,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "1912520982",
    "lockDownStatus": "",
    "latitude": "33.7782",
    "longitude": "76.5762",
    "testCentres": [],
    "markerInfo": [],
    "_i": 33
  },
  {
    "code": "sikkim",
    "name": "SIKKIM",
    "value": 0,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "27.533",
    "longitude": "88.5122",
    "testCentres": [],
    "markerInfo": [],
    "_i": 34
  },
  {
    "code": "uttarakhand",
    "name": "UTTARAKHAND",
    "value": 3,
    "deaths": "0",
    "recoveries": "0",
    "helpline": "104",
    "lockDownStatus": "",
    "latitude": "30.0668",
    "longitude": "70.0193",
    "testCentres": [],
    "markerInfo": [],
    "_i": 35
  }
]

rowC = 1

for row in y:
	markerInfo = row["markerInfo"]
	colC = 1
	for marker in markerInfo:
		val =  str(marker["geometry"]["location"]["lat"]) + ',' + str(marker["geometry"]["location"]["lng"]) + ',' + marker["place_id"]
		sheet.cell(row=rowC, column=colC, value=val)
		colC = colC + 1
	rowC = rowC + 1


workbook.save(filename="./hello_world.xlsx")




