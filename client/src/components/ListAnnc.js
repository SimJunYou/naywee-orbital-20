import React, { Fragment } from "react";
import Typography from '@material-ui/core/Typography';

import AnncTable from './AnncTable'


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