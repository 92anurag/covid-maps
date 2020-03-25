import React from 'react';
import Tabletop from 'tabletop';
import './Map.css';
import MetaDataInfo from './MetadataInfo';

const HighMaps = require('react-highcharts/ReactHighmaps');
const indiaMapData = require('./mapdata/india-all-distributed');


class Maps extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            stateMetadata: null,
            dataAvailable: false
        }
        this.renderDetails = this.renderDetails.bind(this);
    }


    processData(googleData) {
        let data = [...googleData];
  
        data = data.map(function(row) {
            console.log(row);
            let testCentres = [],
                markerInfo = [];

            for (let i = 1; i <= 20; i++) {
                const newKey = 'testingCentre' + i;

                if (row[newKey] !== '' && row[newKey] !== undefined && row[newKey] !== null) {
                    testCentres.push({name: row[newKey], gov: true});
                }
            }

            for (let i = 1; i <= 10; i++) {
                const newKey = 'privateCentre' + i;

                if (row[newKey] !== '' && row[newKey] !== undefined && row[newKey] !== null) {
                    testCentres.push({name: row[newKey], gov: false});
                }
            }

            for (let i = 1; i <= 20; i++) {
                const newKey = 'testingCentreMetadata' + i;

                console.log(newKey);
                if (row[newKey] !== '' && row[newKey] !== undefined && row[newKey] !== null) {  

                    const markerData = row[newKey].split(',');

                    markerInfo.push({
                        lat: parseFloat(markerData[0]),
                        lng: parseFloat(markerData[1]),
                        place_id: markerData[2]
                     });
                }
            }

            for (let i = 1; i <= 20; i++) {
                const newKey = 'privateCentreMetadata' + i;

                if (row[newKey] !== '' && row[newKey] !== undefined && row[newKey] !== null) {

                    const markerData = row[newKey].split(',');

                    markerInfo.push({
                        lat: parseFloat(markerData[0]),
                        lng: parseFloat(markerData[1]),
                        place_id: markerData[2]
                    });
                }
            }

            return {
                code: row.code.toLowerCase(),
                name: row.name,
                value: parseFloat(row.total),
                deaths: row.deaths,
                recoveries: row.recoveries,
                helpline: row.helpline,
                lockDownStatus: row.lockDownStatus,
                latitude: row.latitude,
                longitude: row.longitude,
                testCentres: testCentres,
                markerInfo: markerInfo
            }
        });
        return data;
    }

    getMaxValueStateCode(data) {
        let stateMetadata = null, 
            ma = 0

        if(data !== null && data.length !== 0) {
            stateMetadata = data[0];
            ma = data[0].value;

            for(let i=1;i<data.length;i++) {
                if(ma < data[i].value) {
                    ma = data[i].value;
                    stateMetadata = data[i];
                }
            }
        }
        return stateMetadata;
    }


    componentDidMount() {
        Tabletop.init({
            key: '1dK3kzGfe5Kpn5-DQHQvJ6-qzq_4lNaX8fkfztPhlzfQ',
            simpleSheet: true
        }).then((googleData) => {
            const newData = this.processData(googleData);

            return newData;
        }).then(async (data) => {
            const stateMetadata = this.getMaxValueStateCode(data);

            // for(let idx=0;idx<data.length;idx++) {
            //     const testCentres = data[idx].testCentres;
            //     const markerInfo = [];

            //     for (const place of testCentres) {
            //         const encodePlace = encodeURI(place.name);
            //         const placeUrl = "https://maps.googleapis.com/maps/api/geocode/json?address=" + encodePlace + "&key=AIzaSyBughRH5p8t5wNMDZBR7flrMBlMFSPH67Y";
            //         const response = await axios.get(placeUrl);

            //         markerInfo.push(response.data.results[0]);
            //     }
            //     data[idx]["markerInfo"] = markerInfo;
            // }

            this.data = data;

            window.data = data;

            this.config = {
                chart: {
                    width: window.innerWidth <= 600 ? window.innerWidth : 600, 
                    height: window.innerWidth <= 600 ? (window.innerWidth * 4 / 3) : 800
                },
                title: {
                    text: "COVID India Cases"
                },
                tooltip: {
                    backgroundColor: "#fff",
                    borderWidth: 0,
                    distance: 2,
                    followPointer: false,
                    followTouchMove: false,
                    shadow: false,
                    useHTML: true,
                    pointFormat:
                        '<span class="f32"><span class="flag"></span></span>' +
                        "<span class='f44'> {point.name}: <b>{point.value}</b> cases </span> <br /> <span class='f44'>Deaths: {point.deaths}</span> <br /> <span class='f44'>Recoveries: {point.recoveries}</span>",
                },
                colorAxis: {
                    stops: [
                        [0, '#d5eef7'],
                        [0.1, '#0000FA'],
                        [0.2, '#004DFF'],
                        [0.3, '#00B4FF'],
                        [0.4, '#2CFFCB'],
                        [0.5, '#80FF77'],
                        [0.6, '#D1FF26'],
                        [0.7, '#FFC500'],
                        [0.8, '#FF6800'],
                        [0.9, '#ED0400'],
                        [1, '#880000']
                    ],
                    min: 0
                },
                legend: {
                    title: {
                        text: "Confirmed COVID Cases"
                    },
                    align: "left",
                    verticalAlign: "bottom",
                    valueDecimals: 0,
                    backgroundColor: "rgba(255,255,255,0.9)",
                    symbolRadius: 0,
                    symbolHeight: 14
                },
                series: [{
                    data: data,
                    mapData: indiaMapData,
                    joinBy: null,
                    name: 'Covid',
                    states: {
                        hover: {
                            color: "#07cffc"
                        }
                    },
                    point: {
                        events: {
                            click: function (evt) {
                                var stateMetadata = this.options;
                                console.log(this);
                                this.events.showPopOver(stateMetadata)
                            },
                            showPopOver: (stateMetadata) => {
                                this.setState({
                                    stateMetadata: stateMetadata
                                });
                            }
                        }
                    },
                    dataLabels: {
                        enabled: true,
                        format: "{point.job}"
                    }
                }]
            }
            this.setState({ dataAvailable: true, stateMetadata: stateMetadata });
        });
    }

    renderDetails() {
        return ;
    }

    render() {
        return <div className="india-map-detailed-view">
            {this.state.dataAvailable && <div className="india-map"><HighMaps config={this.config}/></div>}
            {this.state.stateMetadata && <div className="detailed-dialog">
                <MetaDataInfo data={this.state.stateMetadata} />
            </div>}
        </div>
    }
}

export default Maps;