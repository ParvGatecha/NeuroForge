import { create } from "zustand";
import {
  getCurrentUserAction,
  getStreakAction,
  getCompletedLearningItemsAction,
  getBookmarksAction,
  toggleBookmarkAction,
  completeLearningItemAction,
  uncompleteLearningItemAction,
} from "@/app/actions";

interface UserState {
  user: any | null;
  streak: any | null;
  completedLearningItems: number[];
  bookmarks: number[];
  isLoading: boolean;

  fetchUserData: () => Promise<void>;
  toggleBookmark: (learningItemId: number) => Promise<void>;
  completeLearningItem: (learningItemId: number, xpReward: number) => Promise<any>;
  uncompleteLearningItem: (learningItemId: number) => Promise<any>;
}

export const useUserStore = create<UserState>((set, get) => ({
  user: null,
  streak: null,
  completedLearningItems: [],
  bookmarks: [],
  isLoading: false,

  fetchUserData: async () => {
    set({ isLoading: true });
    try {
      const user = await getCurrentUserAction();
      const streak = await getStreakAction();
      const completed = await getCompletedLearningItemsAction();
      const bookmarks = await getBookmarksAction();
      set({ user, streak, completedLearningItems: completed, bookmarks });
    } catch (e) {
      console.error("Error fetching user data in store", e);
    } finally {
      set({ isLoading: false });
    }
  },

  toggleBookmark: async (learningItemId: number) => {
    const { bookmarks } = get();
    const isBookmarked = bookmarks.includes(learningItemId);

    const updated = isBookmarked
      ? bookmarks.filter((id) => id !== learningItemId)
      : [...bookmarks, learningItemId];
    set({ bookmarks: updated });

    try {
      const serverResult = await toggleBookmarkAction(learningItemId);
      if (serverResult !== !isBookmarked) {
        const freshBookmarks = await getBookmarksAction();
        set({ bookmarks: freshBookmarks });
      }
    } catch (e) {
      console.error("Failed to toggle bookmark", e);
      set({ bookmarks });
    }
  },

  completeLearningItem: async (learningItemId: number, xpReward: number) => {
    const { completedLearningItems } = get();
    if (completedLearningItems.includes(learningItemId)) {
      return { success: true, alreadyCompleted: true };
    }

    try {
      const result = await completeLearningItemAction(learningItemId, xpReward);
      const user = await getCurrentUserAction();
      const streak = await getStreakAction();
      const completed = await getCompletedLearningItemsAction();

      set({ user, streak, completedLearningItems: completed });
      return result;
    } catch (e) {
      console.error("Failed to complete learning item", e);
      throw e;
    }
  },

  uncompleteLearningItem: async (learningItemId: number) => {
    const { completedLearningItems } = get();
    if (!completedLearningItems.includes(learningItemId)) {
      return { success: true, alreadyUncompleted: true };
    }

    try {
      const result = await uncompleteLearningItemAction(learningItemId);
      const user = await getCurrentUserAction();
      const streak = await getStreakAction();
      const completed = await getCompletedLearningItemsAction();

      set({ user, streak, completedLearningItems: completed });
      return result;
    } catch (e) {
      console.error("Failed to uncomplete learning item", e);
      throw e;
    }
  },
}));
