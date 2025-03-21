import { ToastOptions, toast } from "react-toastify";

import { CustomSuccessToastElement,
  CustomErrorToastElement,
  CustomWarningToastElement,
  CustomInfoToastElement, } from "./toastElements";

import { CustomToastContainer } from "./toastContainer";

const successToast = (message: string, options?: ToastOptions) => {
  toast.success(<CustomSuccessToastElement message={message} />, {
    closeButton: false,
    hideProgressBar: true,
    autoClose: 1000,
    position: "bottom-left",
    ...options,
  });
};
const errorToast = (
  message: string | undefined | React.ReactNode,
  options?: ToastOptions
) => {
  const toastMessage =
    message ?? "";
  toast.dismiss();
  toast.error(<CustomErrorToastElement message={toastMessage} />, {
    closeButton: false,
    hideProgressBar: true,
    autoClose: 1000,
    position: "bottom-left",
    ...options,
  });
};
const warningToast = (message: string, options?: ToastOptions) => {
  const toastMessage =
    message ?? " ";
  toast.warning(<CustomWarningToastElement message={toastMessage} />, {
    closeButton: false,
    hideProgressBar: true,
    autoClose: 1000,
    position: "bottom-left",
    ...options,
  });
};
const infoToast = (message: string, options?: ToastOptions) => {
  const toastMessage =
    message ?? "";
  toast.info(<CustomInfoToastElement message={toastMessage} />, {
    closeButton: false,
    hideProgressBar: true,
    autoClose: 1000,
    position: "bottom-left",
    ...options,
  });
};

export {
  successToast,
  errorToast,
  warningToast,
  infoToast,
  CustomToastContainer,
};
