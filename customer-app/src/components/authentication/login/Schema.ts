import { Email } from "@mui/icons-material";
import { InferType, object, string } from "yup";

export const Schema = object().shape({
    username: string().required("user name is required"),
    password: string().required("Password is required")
})

export type TScheme = InferType<typeof Schema>;