import axios, { AxiosError, AxiosRequestConfig } from "axios";


const apiEndpoint = process.env.NEXT_PUBLIC_API_ENDPOINT;



const axiosInstance = axios.create({
    baseURL: apiEndpoint,
    headers: {
      "Content-Type": "application/json",
      "Accept-Language": "ja",
    },
  });

const axiosPrivate = axiosInstance;
async function Api(
    path: string,
    request: any,
    method: any,
    params?: object | null,
    headers: any = {},
    otherAxiosProps?: AxiosRequestConfig<object | null> & {
      returnWithAllData?: boolean;
    }
  ) {
    return axiosPrivate({
      data: request,
      method: method,
      url: path,
      params: params,
      headers: headers,
      ...otherAxiosProps,
    }).then((res:any) => {
      if (res) {
        if (otherAxiosProps?.returnWithAllData) {
          return res;
        }
        return res.data;
      } else {
        throw Object.assign(new Error("Invalid Response"), { code: 402 });
      }
    });
  }
  
  export { axiosPrivate,Api };