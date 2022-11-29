import { useTheme } from "@react-navigation/native"
import { useForm } from "react-hook-form"
import { Image, StyleSheet, Text, View } from "react-native"
import { ButtonComponent, TextInputField } from "../../components/"

const viewStyle = StyleSheet.create({
	flex: 1,
	height: "100%",
	width: "100%",
	alignItems: "center",
})

export const Login = () => {
	const { typography } = useTheme()
	const {
		control,
		formState: { errors },
	} = useForm()

	return (
		<View style={{ ...viewStyle, backgroundColor: "white" }}>
			<View
				style={{
					...viewStyle,
					justifyContent: "flex-end",
					marginBottom: 100,
				}}>
				<Image
					source={require("../../assets/images/logo.png")}
					style={{
						resizeMode: "contain",
						maxHeight: 250,
						maxWidth: "100%",
					}}
				/>
				<Text style={{ ...typography.lg, textTransform: "uppercase" }}>
					Escola de Reis
				</Text>
			</View>
			<View
				style={{
					...viewStyle,
					justifyContent: "flex-start",
					width: "90%",
				}}>
				<Text
					style={{
						...typography.sm,
						textTransform: "uppercase",
						marginBottom: 32,
					}}>
					Bem-vindo
				</Text>
				<TextInputField
					control={control}
					name="email"
					errors={errors.email}
					label={"E-mail"}
					placeholder={"exemplo@gmail.com"}
					style={{ width: "100%", marginBottom: 20 }}
				/>
				<TextInputField
					control={control}
					name="password"
					errors={errors.password}
					label={"Senha"}
					placeholder={"*********"}
					style={{ width: "100%", marginBottom: 20 }}
				/>
				<ButtonComponent
					title="Entrar"
					variant="primary"
					size="full"
					onPress={() => console.warn("pressionado")}
				/>
			</View>
		</View>
	)
}
