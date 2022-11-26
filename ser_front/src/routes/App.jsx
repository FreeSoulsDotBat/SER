import { SafeAreaView, View } from "react-native"
import { NavigationContainer } from "@react-navigation/native"
import Stack from "./Stack"
import BottomTab from "./BottomTab"
import { colors } from "../theme/colors"
import { typography } from "../theme/typography"
import { useState } from "react"

const Theme = {
	dark: false,
	colors,
	typography,
	components: {
		button: {
			color: "black",
		},
	},
}

export default App = () => {
	const [loggedIn, setLoggedIn] = useState(false)

	return (
		<SafeAreaView style={{ flex: 1 }}>
			<NavigationContainer theme={Theme}>
				{loggedIn ? <BottomTab /> : <Stack />}
			</NavigationContainer>
		</SafeAreaView>
	)
}
