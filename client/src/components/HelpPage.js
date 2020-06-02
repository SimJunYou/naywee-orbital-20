import React, { Fragment, useState } from "react";
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
  // nothing here yet
});

const HelpPage = () => {
  const classes = useStyles();

  return (
    <Fragment>
      <Typography variant="h3">
        Help
      </Typography>
      <Typography paragraph>
        Here goes the help page! There will be images here as well one day.
        Will probably complete writing this help page once the rest of the site is done...
      </Typography>
    </Fragment>
  );
};
  

export default HelpPage;