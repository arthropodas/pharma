import { styled } from "@mui/material";
import { ToastContainer } from "react-toastify";

// Replace with your preferred custom color values
const customColors = {
  info: "#4CAF50", // Custom info color (green)
  success: "#8BC34A", // Custom success color (light green)
  error: "#F44336", // Custom error color (red)
  warning: "#FF9800", // Custom warning color (orange)
};

export const CustomToastContainer = styled(ToastContainer)(() => ({
  "& .Toastify__toast": {
    boxShadow: "none",
    display: "inline-flex",
    padding: "8px 16px",
    alignItems: "center",
    borderRadius: "8px",
    color: "white",
  },
  "& .Toastify__toast--info": {
    backgroundColor: customColors.info, // Changed background color
  },
  "& .Toastify__toast--success": {
    backgroundColor: customColors.success, // Changed background color
  },
  "& .Toastify__toast--error": {
    backgroundColor: customColors.error, // Changed background color
  },
  "& .Toastify__toast--warning": {
    backgroundColor: customColors.warning, // Changed background color
  },
  "& .Toastify__toast-icon ": {
    display: "none",
  },
  "&.Toastify__toast-container": {
    width: "auto ",
  },
}));
