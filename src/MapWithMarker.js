import React from 'react';
import { Map, Marker, GoogleApiWrapper } from 'google-maps-react';

const mapStyles = {
    width: window.innerWidth >= 460 ? '342px' : `${window.innerWidth - 118}px`,
    height: '300px'
};

export class MapContainer extends React.Component {
    constructor(props) {
        super(props);
        this.renderMarker = this.renderMarker.bind(this);
        this.onMarkerClick = this.onMarkerClick.bind(this);
    }

    onMarkerClick(val, map, clickEvent) {
        this.props.setMarkerInfo(val.keyValue);
    }

    renderMarker() {
        return this.props.data.markerInfo.map((marker, idx) => {
            const lat = marker.lat,
                long = marker.lng;

            return <Marker 
                keyValue={idx}
                disableDoubleClickZoom={true}
                onClick={(val, map, clickEvent) => this.onMarkerClick(val, map, clickEvent)}
                icon={this.props.data.testCentres[idx].gov ? "https://mt.googleapis.com/vt/icon/name=icons/onion/SHARED-mymaps-pin-container-bg_4x.png,icons/onion/SHARED-mymaps-pin-container_4x.png,icons/onion/1899-blank-shape_pin_4x.png&highlight=ff000000,E65100&scale=1.0" : "https://mt.googleapis.com/vt/icon/name=icons/onion/SHARED-mymaps-pin-container-bg_4x.png,icons/onion/SHARED-mymaps-pin-container_4x.png,icons/onion/1899-blank-shape_pin_4x.png&highlight=ff000000,0288D1&scale=1.0"}
                title={this.props.data.testCentres[idx].name}
                name={this.props.data.testCentres[idx].name}
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
                mapTypeId='terrain'
            >
                {this.props.data.markerInfo && this.props.data.markerInfo.length !==0 && this.renderMarker()}
            </Map>
        );
    }
}

export default GoogleApiWrapper({
    apiKey: 'AIzaSyBughRH5p8t5wNMDZBR7flrMBlMFSPH67Y'
})(MapContainer);
