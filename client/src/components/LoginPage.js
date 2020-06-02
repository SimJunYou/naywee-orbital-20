import React, { Fragment, useState } from "react";
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
  // nothing here yet
});

const LoginPage = () => {
  const classes = useStyles();

  return (
    <Fragment>
      <Typography variant="h3">
        Login
      </Typography>
      <Typography paragraph>
        Here goes the login page! :D
      </Typography>
    </Fragment>
  );
};
  

export default LoginPage;