import { LoginRequest, RegisterRequest } from "./types";
import { axiosPrivate } from "./interceptor";

const userRegistration = (data: RegisterRequest) => {
  return axiosPrivate.post("user/register/", data);
};

const userLogin = (data: LoginRequest) => {
  console.log("Inside login service");
  return axiosPrivate.post("auth/login", data);
};

const customerService = { userRegistration, userLogin };

export { customerService };
