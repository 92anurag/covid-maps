import React from 'react';
import { Map, Marker, GoogleApiWrapper } from 'google-maps-react';

const mapStyles = {
    width: '342px',
    height: '300px'
};

export class MapContainer extends React.Component {
    constructor(props) {
        super(props);
        this.renderMarker = this.renderMarker.bind(this);
        this.onMarkerClick = this.onMarkerClick.bind(this);
    }

    onMarkerClick(val) {
        console.log(val)
        this.props.setMarkerInfo(val.keyValue);
    }

    renderMarker() {
        return this.props.data.markerInfo.map((marker, idx) => {
            const lat = marker.geometry.location.lat,
                long = marker.geometry.location.lng;

            return <Marker 
                keyValue={idx}
                onClick={(val) => this.onMarkerClick(val)}
                title={this.props.data.testCentres[idx]}
                name={this.props.data.testCentres[idx]}
                position={{ lat: lat, lng: long}} />
        })
    }

    render() {
        console.log("map data", this.props.data);
        return (
            <Map
                google={this.props.google}
                zoom={5}
                style={mapStyles}
                initialCenter={{
                    lat: this.props.data.latitude,
                    lng: this.props.data.longitude
                }}
                center={{
                    lat: this.props.data.latitude,
                    lng: this.props.data.longitude
                }}
                disableDefaultUI={true}
                gestureHandling='none'
                mapTypeId='terrain'
            >
                {this.props.data.markerInfo && this.props.data.markerInfo.length !==0 && this.renderMarker()}
            </Map>
        );
    }
}

export default GoogleApiWrapper({
    apiKey: 'AIzaSyBoCnvblhgyR0-hqteGlsLs0GlCa5-8jdA'
})(MapContainer);
