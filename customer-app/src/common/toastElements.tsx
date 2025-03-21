import { Stack, Typography } from "@mui/material";

const CustomSuccessToastElement = ({ message }: { message: string }) => {
  return (
    <Stack direction={"row"} gap={1}>
      <span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
        >
          <path
            d="M9.59212 15.9952L18.5824 6.99707L19.9961 8.41205L11.0051 17.411C10.2242 18.1925 8.95813 18.1924 8.17739 17.4107L3.99609 13.2242L5.40983 11.8092L9.59212 15.9952Z"
            fill="white"
          />
        </svg>
      </span>
      <Typography sx={{ whiteSpace: "pre-line" }}>{message}</Typography>
      <span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 20 20"
          fill="none"
        >
          <path
            d="M11.1806 9.99964L16.6683 15.4852L15.4905 16.6655L10.0013 11.1785L4.51124 16.6663L3.3335 15.486L8.822 9.99964L3.33357 4.51337L4.51131 3.33301L10.0013 8.82082L15.4904 3.33382L16.6682 4.51419L11.1806 9.99964Z"
            fill="white"
          />
        </svg>
      </span>
    </Stack>
  );
};

const CustomErrorToastElement = ({
  message,
}: {
  message: string | React.ReactNode;
}) => {
  return (
    <Stack direction={"row"} gap={1}>
      <span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width={24}
          height={24}
          viewBox="0 0 24 24"
          fill="none"
        >
          <path
            d="M12.9961 6.33081V13.6641H10.9961V6.33081H12.9961Z"
            fill="white"
          />
          <path
            d="M12.9961 17.6638V15.6638H10.9961V17.6638H12.9961Z"
            fill="white"
          />
          <path
            fillRule="evenodd"
            clipRule="evenodd"
            d="M11.9961 21.9968C17.5189 21.9968 21.9961 17.5197 21.9961 11.9968C21.9961 6.47398 17.5189 1.99683 11.9961 1.99683C6.47325 1.99683 1.99609 6.47398 1.99609 11.9968C1.99609 17.5197 6.47325 21.9968 11.9961 21.9968ZM11.9961 19.9968C16.4144 19.9968 19.9961 16.4151 19.9961 11.9968C19.9961 7.57855 16.4144 3.99683 11.9961 3.99683C7.57782 3.99683 3.99609 7.57855 3.99609 11.9968C3.99609 16.4151 7.57782 19.9968 11.9961 19.9968Z"
            fill="white"
          />
        </svg>
      </span>
      <Typography whiteSpace={"pre-line"}>{message}</Typography>
      <span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 20 20"
          fill="none"
        >
          <path
            d="M11.1806 9.99964L16.6683 15.4852L15.4905 16.6655L10.0013 11.1785L4.51124 16.6663L3.3335 15.486L8.822 9.99964L3.33357 4.51337L4.51131 3.33301L10.0013 8.82082L15.4904 3.33382L16.6682 4.51419L11.1806 9.99964Z"
            fill="white"
          />
        </svg>
      </span>
    </Stack>
  );
};
const CustomWarningToastElement = ({ message }: { message: string }) => {
  return (
    <Stack direction={"row"} gap={1}>
      <span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width={24}
          height={24}
          viewBox="0 0 24 24"
          fill="none"
        >
          <path
            d="M10.9961 8.99683H12.9961V12.9968H10.9961V8.99683Z"
            fill="white"
          />
          <path
            d="M12.9961 14.9968H10.9961V16.9968H12.9961V14.9968Z"
            fill="white"
          />
          <path
            fillRule="evenodd"
            clipRule="evenodd"
            d="M10.2662 3.0427L2.23773 18.0435C1.5245 19.3762 2.47576 20.9976 3.97082 20.9976L20.0214 20.9977C21.5161 20.9977 22.4674 19.3768 21.7548 18.0442L13.7327 3.0433C12.9867 1.64827 11.0127 1.64793 10.2662 3.0427ZM11.9993 3.99683L3.97083 18.9976L20.0214 18.9977L11.9993 3.99683Z"
            fill="white"
          />
        </svg>
      </span>
      <Typography>{message}</Typography>
      <span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 20 20"
          fill="none"
        >
          <path
            d="M11.1806 9.99964L16.6683 15.4852L15.4905 16.6655L10.0013 11.1785L4.51124 16.6663L3.3335 15.486L8.822 9.99964L3.33357 4.51337L4.51131 3.33301L10.0013 8.82082L15.4904 3.33382L16.6682 4.51419L11.1806 9.99964Z"
            fill="white"
          />
        </svg>
      </span>
    </Stack>
  );
};
const CustomInfoToastElement = ({ message }: { message: string }) => {
  return (
    <Stack direction={"row"} gap={1}>
      <span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width={24}
          height={24}
          viewBox="0 0 24 24"
          fill="none"
        >
          <path
            d="M12.9961 10.9968V17.9968H10.9961V10.9968H12.9961Z"
            fill="white"
          />
          <path
            d="M11.9961 8.99683C12.8245 8.99683 13.4961 8.32525 13.4961 7.49683C13.4961 6.6684 12.8245 5.99683 11.9961 5.99683C11.1677 5.99683 10.4961 6.6684 10.4961 7.49683C10.4961 8.32525 11.1677 8.99683 11.9961 8.99683Z"
            fill="white"
          />
          <path
            fillRule="evenodd"
            clipRule="evenodd"
            d="M11.9961 21.9968C17.5189 21.9968 21.9961 17.5197 21.9961 11.9968C21.9961 6.47398 17.5189 1.99683 11.9961 1.99683C6.47325 1.99683 1.99609 6.47398 1.99609 11.9968C1.99609 17.5197 6.47325 21.9968 11.9961 21.9968ZM11.9961 19.9968C16.4144 19.9968 19.9961 16.4151 19.9961 11.9968C19.9961 7.57855 16.4144 3.99683 11.9961 3.99683C7.57782 3.99683 3.99609 7.57855 3.99609 11.9968C3.99609 16.4151 7.57782 19.9968 11.9961 19.9968Z"
            fill="white"
          />
        </svg>
      </span>
      <Typography>{message}</Typography>
      <span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 20 20"
          fill="none"
        >
          <path
            d="M11.1806 9.99964L16.6683 15.4852L15.4905 16.6655L10.0013 11.1785L4.51124 16.6663L3.3335 15.486L8.822 9.99964L3.33357 4.51337L4.51131 3.33301L10.0013 8.82082L15.4904 3.33382L16.6682 4.51419L11.1806 9.99964Z"
            fill="white"
          />
        </svg>
      </span>
    </Stack>
  );
};
export {
  CustomSuccessToastElement,
  CustomErrorToastElement,
  CustomWarningToastElement,
  CustomInfoToastElement,
};
