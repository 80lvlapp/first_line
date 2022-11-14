import * as React from 'react';
import { styled, useTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import MuiAppBar, { AppBarProps as MuiAppBarProps } from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

import GlobalStyles from '@mui/material/GlobalStyles';
import Box from '@mui/material/Box';

import {
    Link,
} from "react-router-dom";


const drawerWidth = 240;



interface AppBarProps extends MuiAppBarProps {
    open?: boolean;
    //
}

const AppBar = styled(MuiAppBar, {
    shouldForwardProp: (prop) => prop !== 'open',
})<AppBarProps>(({ theme, open }) => ({
    transition: theme.transitions.create(['margin', 'width'], {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
    }),
    ...(open && {
        width: `calc(100% - ${drawerWidth}px)`,
        marginLeft: `${drawerWidth}px`,
        transition: theme.transitions.create(['margin', 'width'], {
            easing: theme.transitions.easing.easeOut,
            duration: theme.transitions.duration.enteringScreen,
        }),
    }),
}));


export default function PersistentDrawerLeft() {
    const theme = useTheme();
    const [open, setOpen] = React.useState(false);
 

    return (
        <Box sx={{ display: 'flex'}}>
            <GlobalStyles styles={{ ul: { margin: 0, padding: 0, listStyle: 'none' } }} />
            <CssBaseline />
            <AppBar
                position="absolute"
                //         color="default"
                elevation={0}
                open={open}
                sx={{ borderBottom: (theme) => `1px solid ${theme.palette.divider}` }}
            >

                <Toolbar sx={{
                    pr: '24px', // keep right padding when drawer closed
                }}>
                    

                    <Typography
                        component={Link}
                        to={"/"}
                        variant="h6"
                        color="inherit"
                        noWrap
                        sx={{ flexGrow: 1 }}
                    >
                        Sports rating
                    </Typography>
                

                </Toolbar>

            </AppBar>
         
        </Box>
    );
}
