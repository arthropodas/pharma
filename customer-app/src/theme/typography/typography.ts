export type TypographyType = {
  fontSize: {
    headXXL: number;
    headXL: number;
    headL: number;
    headM: number;
    headS: number;
    headXS: number;
    body: number;
    button: number;
    caption: number;
  };
  fontWeight: {
    400: string;
    500: string;
    700: string;
    800: string;
  };
};

export const Typography: TypographyType = {
  fontSize: {
    headXXL: 32,
    headXL: 28,
    headL: 24,
    headM: 20,
    headS: 18,
    headXS: 16,
    body: 14,
    button: 16,
    caption: 12,
  },
  fontWeight: {
    400: "400",
    500: "500",
    700: "700",
    800: "800",
  },
};
