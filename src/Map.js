import React from 'react';
import Tabletop from 'tabletop';
import './Map.css';
import detailedViewData from './mapdata/detailed-info';
import { withStyles, makeStyles } from '@material-ui/core/styles';

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
const HighMaps = require('react-highcharts/ReactHighmaps');
const indiaMapData = require('./mapdata/india-all-distributed');



const StyledTableCell = withStyles(theme => ({
    head: {
        backgroundColor: theme.palette.common.black,
        color: theme.palette.common.white,
    },
    body: {
        fontSize: 14,
    },
}))(TableCell);

const StyledTableRow = withStyles(theme => ({
    root: {
        '&:nth-of-type(odd)': {
            backgroundColor: theme.palette.background.default,
        },
    },
}))(TableRow);

const useStyles = makeStyles({
    table: {
        minWidth: 400,
    },
});


function CustomizedTables(props) {
    const classes = useStyles();

    let data = {...props.data},
        stateName = data["State"],
        sourceLink = data['Source'];

    delete data.State;
    delete data.Source;

    return <TableContainer component={Paper}>
        <Table className={classes.table} aria-label="customized table">
            <TableHead>
                <TableRow>
                    <StyledTableCell>State</StyledTableCell>
                    <StyledTableCell align="right">{stateName}</StyledTableCell>
                </TableRow>
            </TableHead>
            <TableBody>
                {Object.keys(data).map(row => (
                    <StyledTableRow key={row}>
                        <StyledTableCell component="th" scope="row">
                            {row}
                        </StyledTableCell>
                        <StyledTableCell align="right">{data[row]}</StyledTableCell>
                    </StyledTableRow>
                ))}
                <StyledTableRow key="source">
                    <StyledTableCell component="th" scope="row">
                        Source
                    </StyledTableCell>
                    <StyledTableCell align="right">{sourceLink}</StyledTableCell>
                </StyledTableRow>
            </TableBody>
        </Table>
    </TableContainer>;
}



class Maps extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            stateName: null,
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
                                        stateName: key
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
        const data = detailedViewData.filter(row => row["State"].toLocaleLowerCase() === this.state.stateName.toLocaleLowerCase());
        
        return <div className="detailed-dialog">
            <CustomizedTables data={data[0]}/>
        </div>;
    }

    render() {
        return <div className="india-map-detailed-view">
            {this.state.dataAvailable && <div className="india-map"><HighMaps config={this.config}/></div>}
            {this.state.stateName && this.renderDetails()}
        </div>
    }
}

export default Maps;