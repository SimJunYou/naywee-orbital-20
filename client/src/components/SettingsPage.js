import React, { Fragment, useState } from "react";
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
  // nothing here yet
});

const SettingsPage = () => {
  const classes = useStyles();

  return (
    <Fragment>
      <Typography variant="h3">
        Settings
      </Typography>
      <Typography paragraph>
        Setting page be here!
      </Typography>
    </Fragment>
  );
};
  

export default SettingsPage;