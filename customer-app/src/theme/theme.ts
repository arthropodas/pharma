// theme.ts
import { createTheme } from '@mui/material/styles';
import { Spacing } from './spacing/spacing';
import { CornerRadius } from './corner-radius/corner-radius';
import { Typography } from './typography/typography';

const theme = createTheme({
  mint: {
    appBarHeight: 64,
    drawerWidth: 240,
    color: {
      pallet: {
        yellow900: '#FFC107',
        yellow800: '#FFEB3B',
        // Add other colors here
      },
      background: {
        uiBackground: '#f0f0f0',
        containerBg: {
          layer1: '#ffffff',
          layer2: '#fafafa',
          layer3: '#f5f5f5',
          layer4: '#eeeeee',
          modal: '#ffffff',
          scrim: 'rgba(0, 0, 0, 0.5)',
        },
      },
      border: {
        high: '#000000',
        medium: '#666666',
        mediumHover: '#888888',
        low: '#cccccc',
        lowOpacity: 'rgba(0, 0, 0, 0.2)',
        disabled: '#e0e0e0',
        highInverse: '#ffffff',
        link: '#1976d2',
        linkHover: '#115293',
        accent: '#ff4081',
      },
      text: {
        high: '#000000',
        medium: '#666666',
        low: '#999999',
        disabled: '#cccccc',
        highInverse: '#ffffff',
        fixedWhite: '#ffffff',
        fixedGray: '#cccccc',
        link: '#1976d2',
        accent: '#ff4081',
      },
    },
    cornerRadius: CornerRadius,
  
    spacing: Spacing,
   
    typography: Typography
  },
});

export default theme;
