'use client'
import React, { useMemo } from "react";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import {
  createTheme,
  ThemeProvider as MUIThemeProvider,
  StyledEngineProvider,
  ThemeProvider,
} from "@mui/material";
import theme from "./theme/theme";
import { CustomToastContainer } from "./common";


function AppTheme({ children }: Readonly<{ children: React.ReactNode }>) {
 

  return (
  
    
      <ThemeProvider theme={theme}>
        
         <LocalizationProvider
            dateAdapter={AdapterDayjs}
            adapterLocale="ja"
          >
       
        {children}
        </LocalizationProvider>
        <CustomToastContainer/>
      </ThemeProvider>
   
   
  );
}

export default AppTheme;
