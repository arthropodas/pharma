export const ThemeBaseSpacing = 4;
const formatSize = (size: number) => `${size}px`;
export type SpacingType = {
  x3s: string;
  xxs: string;
  xs: string;
  s: string;
  m: string;
  l: string;
  xl: string;
  xxl: string;
  x3l: string;
  x4l: string;
};

export const Spacing: SpacingType = {
  x3s: formatSize(ThemeBaseSpacing),
  xxs: formatSize(ThemeBaseSpacing * 2),
  xs: formatSize(ThemeBaseSpacing * 3),
  s: formatSize(ThemeBaseSpacing * 4),
  m: formatSize(ThemeBaseSpacing * 6),
  l: formatSize(ThemeBaseSpacing * 8),
  xl: formatSize(ThemeBaseSpacing * 10),
  xxl: formatSize(ThemeBaseSpacing * 12),
  x3l: formatSize(ThemeBaseSpacing * 16),
  x4l: formatSize(ThemeBaseSpacing * 20),
};
