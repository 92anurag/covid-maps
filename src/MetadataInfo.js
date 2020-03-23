import React from 'react';
import MapWithMarker from './MapWithMarker';

import './MetadataInfo.css'


class MetaDataInfo extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            markerInfoDisplayed: null,
            name: ""
        };
        this.setMarkerInfo = this.setMarkerInfo.bind(this);
        this.getUrl = this.getUrl.bind(this);
    }

    setMarkerInfo(markerInfoId) {
        this.setState({markerInfoDisplayed: markerInfoId});
    }

    static getDerivedStateFromProps(props, state) {
        if (props.data.name !== state.name) {
            return {
                markerInfoDisplayed: props.data.markerInfo.length!==0 ? 0: null,
                name: props.data.name
            };
        }
        return null;
    }

    getUrl() {
        let url = null;

        if(this.state.markerInfoDisplayed != null) {
            const lat = this.props.data.markerInfo[0].geometry.location.lat,
                long = this.props.data.markerInfo[0].geometry.location.lng,
                placeId = this.props.data.markerInfo[0].place_id;
            
            url = `https://www.google.com/maps/search/?api=1&query=${lat},${long}&query_place_id=${placeId}`;
        }
        return url;
    }

    render() {
        const data = this.props.data,
            url = this.getUrl();

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
                {this.state.markerInfoDisplayed!=null && <div className="metadata-info-container-selected-pin-info">
                    <div className="metadata-info-container-selected-pin-info-container">
                        <img src="https://mt.googleapis.com/vt/icon/name=icons/onion/SHARED-mymaps-pin-container-bg_4x.png,icons/onion/SHARED-mymaps-pin-container_4x.png,icons/onion/1899-blank-shape_pin_4x.png&highlight=ff000000,C2185B&scale=1.0" />
                        <div className="metadata-info-container-selected-pin-info-container-name">
                            <p>North Eastern Indira Gandhi Regional Institute of Health & Medical Science</p>
                        </div>
                    </div>
                    <div className="metadata-info-container-selected-pin-info-link">
                        <a href={url} target="_blank">google.map.link</a>
                    </div>
                </div>}
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