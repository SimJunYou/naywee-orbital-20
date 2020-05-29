import React, { Fragment, useState } from "react";
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';

import AnncTable from './AnncTable'

const useStyles = makeStyles({
});


const ListAnnc = () => {
  return (
    <Fragment>
      <Typography variant="h3">
        Past Announcements
      </Typography>
      <Typography variant="subtitle1">
        View, delete, and edit from here!
      </Typography>
      <br />
      <AnncTable />
    </Fragment>
  );
};
  

export default ListAnnc;