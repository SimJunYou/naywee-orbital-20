import React, { Fragment, useState } from "react";
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';

import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';

const useStyles = makeStyles({
  button: {
    marginLeft: 10,
    verticalAlign: 'bottom'
  }
});

const InputAnnc = () => {
  const classes = useStyles();
  const [description, setDescription] = useState("New Announcement");

  const onSubmitForm = async e => {
    e.preventDefault();
    try {
      const body = { description };
      const response = await fetch("http://localhost:5000/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
      });

      window.location = "/"; // refreshes window to show changes
    } catch (err) {
      console.error(err.message);
    }
  };

  return (
    <Fragment>
      <Typography variant="h3">
        New Announcement
      </Typography>
      <Typography variant="subtitle1">
        Enter your new announcements here!
      </Typography>
      <br />
      <form noValidate autoComplete="off" onSubmit={onSubmitForm}>
        <TextField variant="outlined" value={description} onChange={e => setDescription(e.target.value)}/>
        <Button className={ classes.button } type="submit" color="primary" variant="contained">
          Submit
        </Button>
      </form>
    </Fragment>
  );
};
  

export default InputAnnc;