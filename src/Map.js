import React from 'react';
import Tabletop from 'tabletop';
import './Map.css';
import detailedViewData from './mapdata/detailed-info';
import CustomizedTables from './CustomizedTables';
import MetaDataInfo from './MetadataInfo';
// import { Map, GoogleApiWrapper } from 'google-maps-react';

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

        data = data.map(row => {
            return {
                code: row.code.toLowerCase(),
                name: row.name,
                value: parseFloat(row.total),
                deaths: row.deaths,
                recoveries: row.recoveries,
                helpline: row.helpline,
                lockDownStatus: row.lockDownStatus
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
            callback: googleData => {
                const newData = this.processData(googleData),
                    stateMetadata = this.getMaxValueStateCode(newData);
                this.data = newData;
                this.config = {
                    chart: {
                        height: 800
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
                            "<span class='f44'> {point.code}: <b>{point.value}</b> cases </span> <br /> <span class='f44'>Deaths: {point.deaths}</span> <br /> <span class='f44'>Recoveries: {point.recoveries}</span>",
                    },
                    colorAxis: {
                        stops: [
                            [0, '#e8f7e9'],
                            [0.5, '#ea772a'],
                            [1, '#fc1307']
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
                        data: newData,
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
            },
            simpleSheet: true
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