import React from 'react';
import MapWithMarker from './MapWithMarker';

import './MetadataInfo.css'


class MetaDataInfo extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            markerInfo: null,
            name: ""
        };
    }

    setMarkerInfo(markerInfo) {
        console.log("nmarek", markerInfo);
        this.setState({markerInfo: markerInfo});
    }

    static getDerivedStateFromProps(props, state) {
        if (props.data.name !== state.name) {
            return {
                markerInfo: props.data.markerInfo,
                name: props.data.name
            };
        }
        return null;
    }

    render() {
        const data = this.props.data;

        return <div className="metadata-info-container">
            <div className="metadata-info-container-header">
                <p>{this.state.name.toUpperCase()}</p>
            </div>
            <div className="metadata-info-container-body">
                <div className="metadata-info-container-helpline">
                    <p>Helpline No. - {data.helpline}</p>
                </div>
                <hr></hr>
                <div className="metadata-info-container-maps">
                    <MapWithMarker setMarkerInfo={this.setMarkerInfo} data={this.props.data}/>
                </div>
                <hr></hr>
                <div className="metadata-info-container-selected-pin-info">
                    <img src="https://maps.gstatic.com/mapfiles/api-3/images/spotlight-poi2_hdpi.png" />
                </div>
                <hr></hr>
                <div className="metadata-info-container-covid-status">
                    <table className="metadata-info-container-covid-status-table">
                        <tr>
                            <td className="metadata-info-container-covid-status-type">ConfirmedCases:</td>
                            <td className="metadata-info-container-covid-status-value">{data.value}</td>
                        </tr>
                        <tr >
                            <td className="metadata-info-container-covid-status-type">Deaths:</td>
                            <td className="metadata-info-container-covid-status-value">{data.deaths}</td>
                        </tr>
                        <tr>
                            <td className="metadata-info-container-covid-status-type">Recoveries</td>
                            <td className="metadata-info-container-covid-status-value">{data.recoveries}</td>
                        </tr>
                    </table>
                    <div className="metadata-info-container-covid-status-lockdown">
                        <p>state lockdown status: <span className="metadata-info-container-covid-status-lockdown-value">{data.lockDownStatus}</span></p>
                    </div>
                </div>
            </div>
        </div>;
    }
}

export default MetaDataInfo;