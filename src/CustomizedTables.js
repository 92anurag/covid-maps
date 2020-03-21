import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

import { withStyles, makeStyles } from '@material-ui/core/styles';


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

    let data = { ...props.data },
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

export default CustomizedTables;

