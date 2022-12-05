import { useTheme } from "@react-navigation/native"
import { Pressable, Text } from "react-native"

export const LinkComponent = ({ text, optionalStyles, ...rest }) => {
	const { colors, typography } = useTheme()
	return (
		<Pressable {...rest}>
			<Text
				style={{
					...typography.link,
					color: colors.blue,
					...optionalStyles,
				}}>
				{text}
			</Text>
		</Pressable>
	)
}
