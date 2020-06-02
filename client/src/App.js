/* REACT AND REACT ROUTER */
import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useLocation,
  NavLink,
  Redirect
} from "react-router-dom";

/* COMPONENTS */
import InputAnnc from "./components/InputAnnc";
import ListAnnc from "./components/ListAnnc";
import HelpPage from "./components/HelpPage";
import LoginPage from "./components/LoginPage";
import SettingsPage from "./components/SettingsPage";

/* MATERIAL UI */
import { makeStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Link from '@material-ui/core/Link';

/* LISTS */
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemIcon from '@material-ui/core/ListItemIcon';

/* TRANSITIONS */
import Grow from '@material-ui/core/Grow';

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
    display: 'flex'
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
    backgroundColor: theme.palette.background.light
  },
  drawerContainer: {
    overflow: 'auto'
  },
  navItem:{
    color: 'inherit',
    // setting hover color and active color of nav bar items
    '&.active, &:hover, &.active:hover': {
      '& path': {
        fill: theme.palette.primary.main
      },
      '& span': {
        color: theme.palette.primary.main
      }
    }
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
    <NavLink className={classes.navItem} style={{ textDecoration: 'none' }} to={to}>
      <ListItem button >
          <ListItemIcon className={classes.navItem}>{icon}</ListItemIcon>
          <ListItemText className={classes.navItem} primary={primary} />
      </ListItem>
    </NavLink>
    
  );
}

function AppCard(props){
  const classes = useStyles();
  const { apps, path } = props;
  let location = useLocation().pathname;

  // redirects from / to /home
  if (path === '/'){
    return (<Route exact path="/"
      render={() => {
          return (<Redirect to="/home" />)
      }}
    />);
  }

  // puts each app in its own card with a grow transition
  const mapApps = apps.map((EachApp, index) =>
    <Grow in={path === location}>
      <Card key={index} className={classes.appCard} variant='outlined'>
        <CardContent>
          <EachApp />
        </CardContent>
      </Card>
    </Grow>
  );

  return (
    <Route path={path}>
      {mapApps}
    </Route>
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
              <NavBarItem icon={<HomeIcon/>} primary='Home' to='/home' />
              <NavBarItem icon={<SettingsIcon/>} primary='Settings' to='/settings' />
              <NavBarItem icon={<HelpIcon/>} primary='Help' to='/help' />
              <NavBarItem icon={<LoginIcon/>} primary='Login' to='/login' />
            </List>
          </div>
        </Drawer>

        {/* CONTENT GOES HERE! */}
        <main className={classes.content}>
          <Toolbar />
          
          <Switch>
            <AppCard key='loginPage' apps={[LoginPage]} path="/login" />
            <AppCard key='helpPage' apps={[HelpPage]} path="/help" />
            <AppCard key='settingsPage' apps={[SettingsPage]} path="/settings" />
            <AppCard key='homePage' apps={[InputAnnc, ListAnnc]} path="/home" />
            <AppCard key='startPage' apps={[]} path="/" /> {/* for redirection from / to /home */}
          </Switch>
        </main>
      </div>
    </Router>
  );
}