import React from 'react';
import Tabletop from 'tabletop';
import './Map.css';

const HighMaps = require('react-highcharts/ReactHighmaps');
const indiaMapData = require('./mapdata/india-all-distributed');

class Maps extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            keyName: null,
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
                recoveries: row.recoveries
            }
        });
        return data;
    }

    componentDidMount() {
        Tabletop.init({
            key: '1dK3kzGfe5Kpn5-DQHQvJ6-qzq_4lNaX8fkfztPhlzfQ',
            callback: googleData => {
                // console.log('google sheet data --->', googleData)
                const newData = this.processData(googleData)
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
                                    var code = this.code;
                                    this.events.showPopOver(code)
                                },
                                showPopOver: (key) => {
                                    this.setState({
                                        open: true,
                                        keyName: key
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
                this.setState({ dataAvailable: true });
            },
            simpleSheet: true
        });
    }

    renderDetails() {
        return <div className="detailed-dialog"> This contains name {this.state.keyName}</div>
    }

    render() {
        return <div className="india-map-detailed-view">
            {this.state.dataAvailable && <div className="india-map"><HighMaps config={this.config}/></div>}
            {this.state.keyName && this.renderDetails()}
        </div>
    }
}

export default Maps;