/* REACT AND REACT ROUTER */
import React from 'react';
import PropTypes from 'prop-types';
import {
  BrowserRouter as Router,
  Link
} from "react-router-dom";

/* COMPONENTS */
import InputAnnc from "./components/InputAnnc";
import ListAnnc from "./components/ListAnnc";

/* MATERIAL UI */
import { makeStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';

/* LISTS */
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemIcon from '@material-ui/core/ListItemIcon';

/* THEME */
import theme from './theme'

/* ICONS */
import HomeIcon from '@material-ui/icons/HomeOutlined';
import SettingsIcon from '@material-ui/icons/SettingsOutlined';
import HelpIcon from '@material-ui/icons/HelpOutlineOutlined';
import LoginIcon from '@material-ui/icons/VpnKeyOutlined';

/* GLOBAL CONSTANTS */
const drawerWidth = 240;

const useStyles = makeStyles({
  root: {
    display: 'flex',
    fontFamily: '-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif;'
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    marginLeft: drawerWidth,
    backgroundColor: theme.palette.background.light,
    color: theme.palette.primary.main
  },
  drawer: {
    zIndex: theme.zIndex.content + 1,
    width: drawerWidth,
    flexShrink: 0
  },
  drawerPaper: {
    width: drawerWidth,
    backgroundColor: theme.palette.background.light,
    color: theme.palette.primary.main

  },
  drawerContainer: {
    overflow: 'auto'
  },
  navItem:{
    color: theme.palette.primary.main
  },
  // necessary for content to be below app bar
  toolbar: theme.mixins.toolbar,
  content: {
    padding: theme.spacing(3),
    height: '100vh',
    width: '100vw',
    backgroundColor: theme.palette.background.main
  },
  appCard: {
    zIndex: theme.zIndex.content + 1,
    padding: theme.spacing(1),
    'margin-top': theme.spacing(3),
    backgroundColor: theme.palette.paper.main,
    color: theme.palette.paper.contrastText,
    borderColor: theme.palette.primary.main
  }
});

function NavBarItem(props) {
  const classes = useStyles();
  const { icon, primary, to } = props;
  return (
    <Link className={classes.navItem} to={to}>
      <ListItem focusRippleColor='red' touchRippleColor='red' button>
          <ListItemIcon className={classes.navItem}>{icon}</ListItemIcon>
          <ListItemText className={classes.navItem} primary={primary} />
      </ListItem>
    </Link>
  );
}



export default function Layout() {
  const classes = useStyles();

  return (
    <Router>
      <div className={classes.root}>
        {/* TOP TITLE BAR */}
        <AppBar position="fixed" className={classes.appBar}>
          <Toolbar>
            <Typography variant="h6" noWrap>
              NUSMods Telebot Administration Website
            </Typography>
          </Toolbar>
        </AppBar>

        {/* SIDE NAVIGATION BAR */}
        <Drawer
          className={classes.drawer}
          variant="permanent"
          classes={{
            paper: classes.drawerPaper,
          }}
        >
          <Toolbar />
          <div className={classes.drawerContainer}>
            <List>
              <NavBarItem icon={<HomeIcon/>} primary='Home' to='/' />
              <NavBarItem icon={<SettingsIcon/>} primary='Settings' to='/settings' />
              <NavBarItem icon={<HelpIcon/>} primary='Help' to='/help' />
              <NavBarItem icon={<LoginIcon/>} primary='Login' to='/login' />
            </List>
          </div>
        </Drawer>

        {/* CONTENT GOES HERE! */}
        <main className={classes.content}>
          <Toolbar />

          <Card className={classes.appCard} variant='outlined'>
            <CardContent>
              <InputAnnc />
            </CardContent>
          </Card>

          <Card className={classes.appCard} variant='outlined'>
            <CardContent>
              <ListAnnc />
            </CardContent>
          </Card>
          
        </main>
      </div>
    </Router>
  );
}