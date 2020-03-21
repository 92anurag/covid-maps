import React from 'react';
import {Map, GoogleApiWrapper} from 'google-maps-react';


import './MetadataInfo.css'

class MetaDataInfo extends React.Component {
    // constructor(props) {
    //     super(props);
    // }

    render() {
        const data = this.props.data;

        console.log("data", data);
        return <div className="metadata-info-container">
            <div className="metadata-info-container-header">
                <p>{data.name.toUpperCase()}</p>
            </div>
            <div className="metadata-info-container-body">
                <div className="metadata-info-container-helpline">
                    <p>Helpline No. - {data.helpline}</p>
                </div>
                <hr></hr>
                <div className="metadata-info-container-maps">
                    <p>Helpline No. - {data.helpline}</p>
                </div>
                <hr></hr>
                <div className="metadata-info-container-selected-pin-info">
                    <p>Helpline No. - {data.helpline}</p>
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