import { createMuiTheme } from '@material-ui/core/styles';

const palette = {
    primary: {    main: '#FF5138',
                  light: '#ff8a50',
                  dark: '#c41c00',
                  contrastText: '#272534' },
    secondary: {  main: '#8A838B',
                  dark: '#807880'},
    background: { main: '#222324',
                  light: '#292929',
                  contrastText: '#AAAAAA'},
    paper: {      main: '#292929',
                  contrastText: '#AAAAAA'},
    text: {       primary: '#AAAAAA'},
    type: 'dark'
};
const themeName = 'NUSMods Theme';

export default createMuiTheme({ palette, themeName });