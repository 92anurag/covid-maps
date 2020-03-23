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
    }

    onMarkerClick(props, marker, e) {
        this.props.setMarkerInfo();
        console.log(props.extraUrl);
    }

    renderMarker() {
        return this.props.data.markerInfo.map((marker, idx) => {
            const lat = marker.geometry.location.lat,
                long = marker.geometry.location.lng,
                placeId = marker.place_id,
                url = `https://www.google.com/maps/search/?api=1&query=${lat},${long}&query_place_id=${placeId}`;

            return <Marker 
                keyValue={idx}
                onClick={this.onMarkerClick}
                title={this.props.data.testCentres[idx]}
                name={'SOMA'}
                extraUrl={url}
                position={{ lat: lat, lng: long}} />
        })
    }

    render() {
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
