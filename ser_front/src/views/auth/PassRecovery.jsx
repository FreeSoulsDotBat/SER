import { useTheme } from "@react-navigation/native"
import { useForm } from "react-hook-form"
import { Image, StyleSheet, Text, View } from "react-native"
import { BaseView, TextInputField } from "../../components"

export const PassRecovery = ({}) => {
	const { colors, typography } = useTheme()

	const {
		control,
		formState: { errors },
	} = useForm()

	const viewStyle = StyleSheet.create({
		flex: 1,
		height: "100%",
		alignItems: "center",
	})
	return (
		<BaseView opitionalStyle={{ paddingTop: 200 }}>
			<View
				style={{
					...viewStyle,
					justifyContent: "flex-start",
					marginBottom: 80,
				}}>
				<Image
					source={require("../../assets/images/logo.png")}
					style={{
						resizeMode: "contain",
						maxHeight: 150,
						maxWidth: "100%",
						marginBottom: 40,
					}}
				/>
				<Text
					style={{
						...typography.md,
						marginBottom: 10,
					}}>
					Recuperação de senha
				</Text>
				<Text
					style={{
						...typography.p,
					}}>
					Informe o e-mail cadastrado para recuperar a senha.
				</Text>
			</View>
			<View
				style={{
					...viewStyle,
					justifyContent: "flex-start",
					width: "90%",
				}}>
				<TextInputField
					control={control}
					name="email"
					errors={errors.email}
					label={"E-mail"}
					placeholder={"exemplo@gmail.com"}
					style={{ width: "100%" }}
				/>
			</View>
		</BaseView>
	)
}
