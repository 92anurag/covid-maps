import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

export default class AlertDialog extends React.Component {

    constructor(props) {
        this.state = {
            showDialog: false
        }
    } 


    static getDerivedStateFromProps(props, state) {
        if (props.showDialog !== state.showDialog) {
            return {
                showDialog: props.showDialog,
            };
        }

        // Return null if the state hasn't changed
        return null;
    }

    handleClose() {
        this.setState({open: false});
    }
    

    return <Dialog 
        open={this.state.open}
        onClose={this.handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
    >
        <DialogTitle id="alert-dialog-title">{"Use Google's location service?"}</DialogTitle>
        <DialogContent>
            <DialogContentText id="alert-dialog-description">
                Let Google help apps determine location. This means sending anonymous location data to
                Google, even when no apps are running.
            </DialogContentText>
        </DialogContent>
    </Dialog>;
}