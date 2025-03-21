import { CornerRadiusType } from './corner-radius/corner-radius';
import { SpacingType } from './spacing/spacing';
import { TypographyType } from './typography/typography';

declare module '@mui/material/styles' {
  interface Theme {
    mint: {
      spacing: SpacingType;
      cornerRadius: CornerRadiusType;
 
      typography: TypographyType;
      appBarHeight: number;
      drawerWidth: number;
      color: {
        pallet: {
          yellow900: string;
          yellow800: string;
        };
        background: {
          uiBackground: string;
          containerBg: {
            layer1: string;
            layer2: string;
            layer3: string;
            layer4: string;
            modal: string;
            scrim: string;
          };
        };
        border: {
          high: string;
          medium: string;
          mediumHover: string;
          low: string;
          lowOpacity: string;
          disabled: string;
          highInverse: string;
          link: string;
          linkHover: string;
          accent: string;
        };
        text: {
          high: string;
          medium: string;
          low: string;
          disabled: string;
          highInverse: string;
          fixedWhite: string;
          fixedGray: string;
          link: string;
          accent: string;
        };
      };
     
    };
  }

  interface ThemeOptions {
    mint?: {
      spacing?: Partial<SpacingType>;
      cornerRadius: Partial<CornerRadiusType>;
 
      typography: Partial<TypographyType>;
      appBarHeight?: number;
      drawerWidth?: number;
      color?: {
        pallet?: {
          yellow900?: string;
          yellow800?: string;
        };
        background?: {
          uiBackground?: string;
          containerBg?: {
            layer1?: string;
            layer2?: string;
            layer3?: string;
            layer4?: string;
            modal?: string;
            scrim?: string;
          };
        };
        border?: {
          high?: string;
          medium?: string;
          mediumHover?: string;
          low?: string;
          lowOpacity?: string;
          disabled?: string;
          highInverse?: string;
          link?: string;
          linkHover?: string;
          accent?: string;
        };
        text?: {
          high?: string;
          medium?: string;
          low?: string;
          disabled?: string;
          highInverse?: string;
          fixedWhite?: string;
          fixedGray?: string;
          link?: string;
          accent?: string;
        };
      };
     
    };
  }
}
