import React from "react";
import {
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  FormHelperText,
} from "@mui/material";
import { Control, Controller, FieldError } from "react-hook-form";

interface Option {
  value: string | number;
  label: string;
}

interface CustomSelectProps {
  name: string;
  label: string;
  options: Option[];
  control: Control<any>; // Replace 'any' with your form schema type if using TypeScript
  error?: FieldError;
}

const CustomSelect: React.FC<CustomSelectProps> = ({
  name,
  label,
  options,
  control,
  error,
}) => {
  return (
    <FormControl fullWidth error={!!error}>
      <InputLabel >{label}</InputLabel>
      <Controller
        name={name}
        control={control}
        defaultValue={''} 
        render={({ field }) => (
          <Select {...field} label={label}>
            {options.map((option) => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))}
          </Select>
        )}
      />
      {error && <FormHelperText>{error.message}</FormHelperText>}
    </FormControl>
  );
};

export default CustomSelect;
