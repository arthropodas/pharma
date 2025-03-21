import { TextField, TextFieldProps } from '@mui/material';
import { Control, Controller, FieldErrors } from 'react-hook-form';

interface CustomInputFieldProps extends Omit<TextFieldProps, 'name'> {
  name: string;
  control: Control<any>; 
  errors?: FieldErrors<any>; 
}

const CustomInputField: React.FC<CustomInputFieldProps> = ({
  name,
  control,
  errors,
  ...textFieldProps
}) => {
  return (
    <Controller
      name={name}
      control={control}
      defaultValue={''} 
      render={({ field }) => (
        <TextField
          {...field}
          {...textFieldProps}
          error={!!errors?.[name]}
          helperText={errors?.[name]?.message as string || ''} // Extract only the message
          fullWidth
          
        />
      )}
    />
  );
};

export default CustomInputField;
