import React from 'react';
import Dialog from '@material-ui/core/Dialog';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Popover from '@material-ui/core/Popover';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';

import './App.css';
const HighMaps = require('react-highcharts/ReactHighmaps');
const Highcharts = require('highcharts')
const indidaMapData = require('./mapdata/india');

const useStyles = makeStyles(theme => ({
    typography: {
        padding: theme.spacing(10),
    },
}));
const classes = useStyles();




const indiaCurrentData = [
    ['in-an', 0],
    ['in-wb', 1],
    ['in-ld', 2],
    ['in-5390', 3],
    ['in-py', 4],
    ['in-3464', 5],
    ['in-mz', 6],
    ['in-as', 7],
    ['in-pb', 8],
    ['in-ga', 9],
    ['in-2984', 10],
    ['in-jk', 11],
    ['in-hr', 12],
    ['in-nl', 13],
    ['in-mn', 14],
    ['in-tr', 15],
    ['in-mp', 16],
    ['in-ct', 17],
    ['in-ar', 18],
    ['in-ml', 19],
    ['in-kl', 20],
    ['in-tn', 21],
    ['in-ap', 22],
    ['in-ka', 23],
    ['in-mh', 24],
    ['in-or', 25],
    ['in-dn', 26],
    ['in-dl', 27],
    ['in-hp', 28],
    ['in-rj', 29],
    ['in-up', 30],
    ['in-ut', 31],
    ['in-jh', 32],
    ['in-ch', 33],
    ['in-br', 34],
    ['in-sk', 35]
];

class Info extends React.Component {

    render() {
        return <div>No cases present in this region</div>;
    }
}

class Maps extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            showDialog: false,
            stateName: ''
        }
        this.handleClose = this.handleClose.bind(this);
        this.config = {
            tooltip: {
                distance: 2,
                followPointer: false, 
                followTouchMove: false,
                backgroundColor: "#fff",
                borderWidth: 0,
                shadow: false
            },
            // colorAxis: {
            //     min: 0,
            //     stops: [
            //         [0, '#EFEFFF'],
            //         [0.5, Highcharts.getOptions().colors[3]],
            //         [1, Highcharts.color(Highcharts.getOptions().colors[3]).brighten(-0.5).get()]
            //     ]
            // },
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
                data: indiaCurrentData.map(val => {return {key: val[0], value: val[1]}}),
                mapData: indidaMapData,
                joinBy: ['hc-key', 'key'],
                name: 'Covid',
                states: {
                    hover: {
                        color: Highcharts.getOptions().colors[3]
                    }
                },
                point: {
                    events: {
                        click: function(evt) {
                            var key = this.key;
                            this.events.showDialogBox(key)
                        },
                        showDialogBox: (key) => {
                            this.setState({
                                stateName: key,
                                showDialog: true
                            });
                        }
                    }
                }
            }]
        }
    }

    handleClose() {
        this.setState({ showDialog: false });
    }

    render() {
        return <div>
            <HighMaps config={this.config} />
            {/* <Dialog
                open={this.state.showDialog}
                onClose={this.handleClose}
                aria-labelledby="alert-dialog-title"
                aria-describedby="alert-dialog-description"
            >
                <DialogTitle id="alert-dialog-title">{"Covid Detail State info"}</DialogTitle>
                <DialogContent>
                    <DialogContentText id="alert-dialog-description">
                        <Info />
                    </DialogContentText>
                </DialogContent>
            </Dialog>; */}
            <div className="dummyClick" ref={ref => {
                this.dummyDiv = ref;}}></div>
            <Popover
                open={this.state.showDialog}
                anchorEl={this.dummyDiv}
                onClose={this.handleClose}
                anchorOrigin={{
                    vertical: 'bottom',
                    horizontal: 'center',
                }}
                transformOrigin={{
                    vertical: 'top',
                    horizontal: 'center',
                }}
            >
                <Typography className={classes.typography}>The content of the Popover.</Typography>
            </Popover>
        </div>
    }
}

export default Maps;